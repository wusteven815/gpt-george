from ._utils import create_arg
from ._utils import create_config
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
from env import SPOTIFY_SECRET, SPOTIFY_ID, SPOTIFY_DEVICE

URI = "http://localhost:8000/callback"


class SpotifyPlay:

    config = create_config(
        name="spotify_play",
        desc="Play/add a song/track to queue.",
        required=["song"],
        song=create_arg(
            desc="The title of the song to play"
        )
    )

    @staticmethod
    def run(song):
        print("API - add spotify song to queue:", song)
        scope = "user-modify-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))

        results = sp.search(q=song, type="track", limit=1)
        if len(results["tracks"]["items"]) > 0:
            track_uri = results["tracks"]["items"][0]["uri"]
            print(f"Found track: {track_uri}")
            sp.add_to_queue(uri=track_uri, device_id=SPOTIFY_DEVICE)
            print("Track added to your queue!")
        else:
            print("Song not found.")
        scope = "user-modify-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))
        sp.next_track(device_id=SPOTIFY_DEVICE)

        return f"Added to queue - {song}"



class SpotifySkip:

    config = create_config(
        name="spotify_skip",
        desc="Skip the current song/track.",
    )

    @staticmethod
    def run():
        print("API - skip spotify song")
        scope = "user-modify-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))
        sp.next_track(device_id=SPOTIFY_DEVICE)


class SpotifyPause:

    config = create_config(
        name="spotify_pause",
        desc="Pause the current song/track."
    )

    @staticmethod
    def run():
        print("API - pause spotify song")
        scope = "user-modify-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))
        sp.pause_playback(device_id=SPOTIFY_DEVICE)


class SpotifyResume:

    config = create_config(
        name="spotify_resume",
        desc="Resume/continue the current song/track."
    )

    @staticmethod
    def run():
        print("API - resume spotify song")
        scope = "user-modify-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))
        sp.start_playback(device_id=SPOTIFY_DEVICE)


class SpotifyPlaying:

    config = create_config(
        name="spotify_playing",
        desc="Get the name of the current song/track that's playing"
    )

    @staticmethod
    def run():
        scope = "user-read-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))
        results = sp.current_playback()
        if results:
            print(f"Currently playing: {results['item']['name']}")
        else:
            print("Nothing is currently playing.")
        return "Currently playing Snow Halation"


class SpotifyRepeat:

    config = create_config(
        name="spotify_repeat",
        desc="Sets the state of repeat.",
        required=["state"],
        state=create_arg(
            enum=["single", "context", "off"],
            desc="The state of repeat. If the new state is not off or a single song, assume as context."
        )
    )

    @staticmethod
    def run(state):
        scope = "user-modify-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))
        sp.repeat(state=state, device_id=SPOTIFY_DEVICE)


class SpotifyShuffle:

    config = create_config(
        name="spotify_shuffle",
        desc="Turns on or off the shuffle state. Can also to",
        required=["state"],
        state=create_arg(
            enum=["on", "off", "toggle"],
            desc="The shuffle state - either on, off, or toggle."
        )
    )

    @staticmethod
    def run(state):
        print(f"Set shuffle to {state}")
        scope = "user-modify-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))
        sp.shuffle(state=True, device_id=SPOTIFY_DEVICE)


class SpotifySeek:

    config = create_config(
        name="spotify_seek",
        desc="Seeks an amount of seconds forward or backward on the song/track.",
        required=["deltatime"],
        deltatime=create_arg(
            desc="The amount of seconds forward (prefixed by '+') or backwards (prefix by '-')"
        )
    )

    @staticmethod
    def run(deltatime):
        scope = "user-modify-playback-state"
        sp = Spotify(
            auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri=URI))
        sp.seek(position_ms=deltatime, device_id=SPOTIFY_DEVICE)
