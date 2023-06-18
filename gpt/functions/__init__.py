from .email import *
from .spotify import *


details = [
    EmailSend,
    SpotifyPlay, SpotifySkip, SpotifyPause, SpotifyResume, SpotifyPlaying, SpotifyRepeat, SpotifyShuffle, SpotifySeek,
]

configs = []
functions = {}

for detail in details:
    configs.append(detail.config)
    functions[detail.config["name"]] = detail.run
