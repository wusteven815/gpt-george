from threading import Thread
from audio import start_audio_task
from ui import start_ui_task


user_text = "Starting up..."
gpt_text = ""


def get_text():
    return user_text, gpt_text


def set_text(which, new):
    global user_text
    global gpt_text
    if which == "user":
        user_text = new
    elif which == "gpt":
        print("new gpt", new)
        gpt_text = new


if __name__ == "__main__":

    audio_thread = Thread(target=start_audio_task, args=(set_text,))
    ui_thread = Thread(target=start_ui_task, args=(get_text,))

    audio_thread.start()
    ui_thread.start()

    audio_thread.join()
    ui_thread.join()
