from distutils.core import setup

setup(
    name = 'scdl',
    packages = ['scdl'],
    version = '0.1.0',
    description = 'Simple Soundcloud Downloader',
    author='Joe Engelman',
    author_email = "engelman.joe@gmail.com",
    url = "https://github.com/joengelm/scdl",
    download_url = "https://github.com/joengelm/scdl/archive/v0.1.0.zip",
    keywords = ["soundcloud", "download", "music", "streaming", "simple"],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        ],
    long_description = """\
SCDL: A simple, yet powerful Soundcloud Downloader
--------------------------------------------------

What?
SCDL is a basic library for downloading tracks and playlists from Soundcloud. With one call to 'scdl.download', you can easily save a track or playlist to your computer. SCDL also provides informative output about a song's download progress and embeds each track's artwork into its mp3 file. By default, SCDL will download tracks into the user's '~/Music/Soundcloud/artist/' folder, where artist is the owner of the track (not necessarily the actual artist of the song).

Why?
SCDL provides a jumping off point which is simple enough for nearly all programmers to understand. Anyone can create a Python script that uses SCDL to augment their applications or to create entirely new Soundcloud apps.

Example:

    from scdl import download
    url = 'https://soundcloud.com/joeengelman/lion-king-for-drum-corps'
    dest = './Soundcloud/'
    download(url, dest, silent=False) # The silent argument is optional and, if true, disables progress output
    # That's it! You've just downloaded a song from Soundcloud.

You can also use scdl.py with command line arguments:

    python scdl.py 'https://soundcloud.com/joeengelman'
    python scdl.py 'https://soundcloud.com/joeengelman/lion-king-for-drum-corps'
    python scdl.py 'https://soundcloud.com/joeengelman/sets/winter-2015'

Note: scdl.py can handle an arbitrary number of arguments, and it will download each one in turn.

This version requires Python 2.x. It has not been tested with Python 3.
"""
)