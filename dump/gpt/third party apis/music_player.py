CLIENT_ID = "a0b604295381414db696039c8733368d"
CLIENT_SECRET = "ee00319c46af48f6a898f2339612c742"
URI = "http://localhost:8000/callback"
DEVICE_ID = "90ad67d62cc91f4a155fb9c8a2b338fc1994306d"

import spotipy
from spotipy.oauth2 import SpotifyOAuth

def getDevices():
    scope = "user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))
    devices = sp.devices()
    for device in devices['devices']:
        print(f"Device ID: {device['id']}")
        print(f"Device Name: {device['name']}")
        print('---')


def addSongToQueue(title):
    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))

    results = sp.search(q=title, type="track", limit=1)
    if len(results["tracks"]["items"]) > 0:
        track_uri = results["tracks"]["items"][0]["uri"]
        print(f"Found track: {track_uri}")
        sp.add_to_queue(uri=track_uri, device_id=DEVICE_ID)
        print("Track added to your queue!")
    else:
        print("Song not found.")



def skipTrack():
    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))
    sp.next_track(device_id=DEVICE_ID)


def pauseTrack():
    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))
    sp.pause_playback(device_id=DEVICE_ID)


def setRepeat(state):
    # state is one of: 'track', 'context', 'off'
    # i dont know what each of those even means 
    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))
    sp.repeat(state=state, device_id=DEVICE_ID)

def seekTrack(position):
    # position is in milliseconds
    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))
    sp.seek(position_ms=position, device_id=DEVICE_ID)


def getCurrentlyPlaying():
    scope = "user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))
    results = sp.current_playback()
    if results:
        print(f"Currently playing: {results['item']['name']}")
    else:
        print("Nothing is currently playing.")

def shuffle():
    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))
    sp.shuffle(state=True, device_id=DEVICE_ID)

def startPlayback(): # i think also for unpause it's this
    scope = "user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=URI))
    sp.start_playback(device_id=DEVICE_ID)





addSongToQueue("snow halation")