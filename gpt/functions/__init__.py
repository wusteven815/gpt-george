from .email import *
from .spotify import *
from .maps import *
from .weather import *
from .math import *
from .news import *

details = [
    EmailSend,
    SpotifyPlay, SpotifySkip, SpotifyPause, SpotifyResume, SpotifyPlaying, SpotifyRepeat, SpotifyShuffle, SpotifySeek,
    LocationsGet,
    WeatherGet,
    MathMode,
    NewsGet,
]

configs = []
functions = {}

for detail in details:
    configs.append(detail.config)
    functions[detail.config["name"]] = detail.run
