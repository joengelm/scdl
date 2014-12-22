SCDL: a simple, powerful Soundcloud downloader
==============================================

What?
-----
SCDL is a basic library for downloading tracks and playlists from Soundcloud. With one call to 'scdl.download', you can easily save a track or playlist to your computer. SCDL also provides informative output about a song's download progress and embeds each track's artwork into its mp3 file.

How?
----
SCDL uses the [Soundcloud API Python wrapper](https://github.com/soundcloud/soundcloud-python) and [Mutagen libraries](https://mutagen.readthedocs.org/en/latest/). **Be sure to put your *own* client ID into scdl.py.** You can acquire a client ID easily by going to [Soundcloud's app registration page](http://soundcloud.com/you/apps/new).

Why?
----
SCDL provides a jumping off point which is simple enough for nearly all programmers to understand. Anyone can create a Python script that uses SCDL to augment their applications or to create entirely new Soundcloud apps.

Example
-------
    from scdl import download
    url = 'https://soundcloud.com/joeengelman/lion-king-for-drum-corps'
    dest = './Soundcloud/'
    download(url, dest, silent=False) # The silent argument is optional and, if true, disables progress output
    # That's it! You've just downloaded a song from Soundcloud.
You can also use scdl.py with command line arguments:
    
    python scdl.py 'https://soundcloud.com/joeengelman/lion-king-for-drum-corps'
    
Note: scdl.py can handle an arbitrary number of arguments, and it will download each one in turn.

Scrawl
------
Scrawl is an example program that uses SCDL to crawl Soundcloud and download recommended tracks using a breadth-first search. You can learn more by viewing the comments in scrawl.py.

Troubleshooting
---------------
**Remember to put your *own* client ID into scdl.py.** You can acquire a client ID easily by going to [Soundcloud's app registration page](http://soundcloud.com/you/apps/new).

TODO
----
- Speed up Scrawl
- Implement a timer that measures time spent processing pages/files and time spent interacting with the Soundcloud API
