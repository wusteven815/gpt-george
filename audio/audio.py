import wave
import os
import threading
import audioop
from collections import deque
import openai
import math
import keyboard
import numpy
import pvporcupine
import pyaudio
from pvrecorder import PvRecorder
from gpt import GPTHandler
from env import PORCUPINE_KEY, OPENAI_KEY, AZURE_KEY, AZURE_REGION
import azure.cognitiveservices.speech as speechsdk
from os import system
from Hume import hume_controller

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
SILENCE_LIMIT = 0.4
PREV_AUDIO = 0.2  # Previous audio (in seconds) to prepend. When noise is detected, how much of previously recorded
FILENAME = "input.wav"
RESPONSE = ''
openai.api_key = OPENAI_KEY


# audio is prepended. This helps to prevent chopping the beginning of the phrase.
def audio_int(num_samples=50):
    """ Gets average audio intensity of your mic sound. You can use it to get
        average intensities while you're talking and/or silent. The average
        is the avg of the 20% largest intensities recorded.
    """

    # print("Getting intensity values from mic.")
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # values = [math.sqrt(abs(audioop.avg(stream.read(CHUNK), 2)))
    #           for x in range(num_samples)]
    # values = sorted(values, reverse=True)
    # r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
    # print(" Finished ")
    # print(" Average audio intensity is ", r)

    values = []
    for i in range(num_samples):
        values.append(audioop.rms(stream.read(CHUNK), 2))
    rms = numpy.mean(values)

    decibel = 20 * math.log10(rms)

    stream.close()
    p.terminate()

    return decibel + 5


def listening(threshold):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    recorded_audio = []
    rel = int(RATE / CHUNK)
    slid_win = deque(maxlen=int(SILENCE_LIMIT * rel))
    prev_audio = deque(maxlen=int(PREV_AUDIO * rel))
    started = False

    while True:
        cur_data = stream.read(CHUNK)
        rms = audioop.rms(cur_data, 2)
        if rms == 0:
            rms = threshold
        db = 20 * math.log10(rms)
        slid_win.append(db)
        # print(sum([x > threshold for x in slid_win]))
        if keyboard.is_pressed("enter"):
            break
        if sum([x > threshold for x in slid_win]) > 0:
            if not started:
                # print("Starting record of phrase")
                started = True
            recorded_audio.append(cur_data)
        elif started is True:
            break
        else:
            prev_audio.append(cur_data)
    save_record(list(prev_audio) + recorded_audio, p)
    print("GeorgeAI done recording")

    stream.close()
    p.terminate()


def save_record(data, p):
    # Saves mic data to temporary WAV file.
    file = wave.open(FILENAME, "wb")
    file.setnchannels(CHANNELS)
    file.setsampwidth(p.get_sample_size(FORMAT))
    file.setframerate(RATE)

    file.writeframes(b''.join(data))
    file.close()


# Transcribe audio
def transcribe_audio(filename):
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript["text"]


def azure_speak(response):
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_KEY,
                                           region=AZURE_REGION)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    speech_config.speech_synthesis_voice_name = 'en-US-GuyNeural'
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_text_async(response).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"S{speech_synthesis_result}")


def start_audio_task():

    gpt = GPTHandler()

    threshold = audio_int()
    print(f"Ready - threshold is: {threshold}")
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_KEY,
        keyword_paths=["audio/HeyGeorge.ppn"])

    recorder = PvRecorder(
        device_index=0,
        frame_length=porcupine.frame_length)

    while True:
        recorder.start()

        try:
            while True:
                pcm = recorder.read()
                result = porcupine.process(pcm)

                if result >= 0:
                    recorder.stop()

                    listen_thread = threading.Thread(target=listening, args=(threshold,))
                    listen_thread.start()

                    print("GeorgeAI recording voice - press enter to stop early")

                    listen_thread.join()
                    # send the wav file to hume here
                    response = transcribe_audio(FILENAME)
                    print(response)
                    chatbot = hume_controller.get_result()
                    RESPONSE = response
                    azure_speak(response)

                    break
        except KeyboardInterrupt:
            print('GPTGeorge shutting down')
            break
    recorder.delete()
    porcupine.delete()
