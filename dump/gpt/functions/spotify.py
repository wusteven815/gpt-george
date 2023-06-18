from functions._utils import create_arg
from functions._utils import create_config


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
        return f"Now playing - {song}"


class SpotifySkip:

    config = create_config(
        name="spotify_skip",
        desc="Skip the current song/track.",
    )

    @staticmethod
    def run():
        print("API - skip spotify song")


class SpotifyPause:

    config = create_config(
        name="spotify_pause",
        desc="Pause the current song/track."
    )

    @staticmethod
    def run():
        print("API - pause spotify song")


class SpotifyResume:

    config = create_config(
        name="spotify_resume",
        desc="Resume/continue the current song/track."
    )

    @staticmethod
    def run():
        print("API - resume spotify song")


class SpotifyPlaying:

    config = create_config(
        name="spotify_playing",
        desc="Get the name of the current song/track that's playing"
    )

    @staticmethod
    def run():
        print("API - currently playing")
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
        print(f"Set repeat to {state}")


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
        print(f"Seek {deltatime}s")
