#! /usr/bin/env python
 
#usage : python scdl.py <soundcloud track/playlist url>
 
import soundcloud
import urllib
import re
import time
import os
import sys

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
 
CLIENT_ID = '49009eb8904b11a2a5d2c6bdc162dd32'
MEDIA_STREAM_URL = 'http://media.soundcloud.com/stream/'
 
class scdl:
	client = soundcloud.Client(client_id=CLIENT_ID)
 
	def __init__(self, url, download_path, silent=True):
		self.url = url
		self.download_progress = 0
		self.download_path = download_path
		self.current_time = time.time()
		self.resolveMedia = self.resolve(url)
		self.track_url_dicts = self.get_track_stream_and_image_urls(self.resolveMedia)
		self.silent = silent
 
	# resolve a Soundcloud URL 
	# return track details in list (i.e. if only a single song, 
	#	a single element list will be returned)
	def resolve(self, url):
		returnMedia = []
		resolved_url = self.client.get('/resolve', url=url);
		if resolved_url.kind == 'track':
			# resolved_url is a single track object 
			returnMedia.append(self.get_track_detail(resolved_url.id))	
		elif resolved_url.kind == 'playlist':
			# resolve_url is a list of song objects
			for track in resolved_url.tracks:
				returnMedia.append(self.get_track_detail(track['id']))
		return returnMedia
 
 	# return a dict of important attributes for a specific track
	def get_track_detail(self, track_id):
		track = self.client.get('/tracks/' + str(track_id))
		track_detail = {'title':track.title, 
					 	'waveform_url':track.waveform_url, 
					 	'artwork_url':(track.artwork_url if track.artwork_url else track.user['avatar_url'])}
		return track_detail
 
	# get direct streaming url from waveform url and save it in a dict
	#	with the track title and track artwork url
	# returns a list of ^these dicts
	def get_track_stream_and_image_urls(self, tracks):
		track_stream_and_image_urls = []
		regex = re.compile('\/([a-zA-Z0-9]+)_')
		for track in tracks:
			stream_id = regex.search(track['waveform_url']).groups()[0]	# split URL to find ID
			media_url = MEDIA_STREAM_URL + str(stream_id)
			track_stream_and_image_urls.append({'title':track['title'], 
												'stream_url':media_url, 
												'artwork_url':track['artwork_url']})
		return track_stream_and_image_urls

	def dl_tracks(self, tracks):
		track_filename_list = []
		if not os.path.isdir(self.download_path):
			os.mkdir(self.download_path)
		for track in tracks:
			try:
				track_filename = self.download_path + "{0}.mp3".format(track['title'])
				artwork_filename = self.download_path + ".{0}-artwork.jpg".format(track['title'])
				sys.stdout.write("Downloading: {0}\n".format(track['title']))
				urllib.urlretrieve(url=track['stream_url'], filename=track_filename, reporthook=(None if self.silent else self.dl_progress))
				if not self.silent: print
				urllib.urlretrieve(url=track['artwork_url'], filename=artwork_filename)
				embed_artwork(track_filename, artwork_filename)
				os.remove(artwork_filename)
				track_filename_list.append(track_filename)
			except:
				continue
		return track_filename_list

	def dl_progress(self, block_no, block_size, file_size):
		self.download_progress += block_size
		if int(self.download_progress / 1024 * 8) > 1000:
			speed = "{0} Mbps".format(round((self.download_progress / 1024 / 1024 * 8) / (time.time() - self.current_time), 2))
		else:
			speed = "{0} Kbps".format(round((self.download_progress / 1024 * 8) / (time.time() - self.current_time), 2))
		rProgress = round(self.download_progress / 1024.00 / 1024.00, 2)
		rFile = round(file_size / 1024.00 / 1024.00, 2)
		percent = round(100 * float(self.download_progress) / float(file_size))
		sys.stdout.write("\r {3} ({0:.2f}/{1:.2f}MB): {2:.2f}%".format(rProgress, rFile, percent, speed))
		sys.stdout.flush()

def embed_artwork(track_filename, artwork_filename):
	audio = MP3(track_filename, ID3=ID3)
	# add ID3 tag if it doesn't exist
	try:
	    audio.add_tags()
	except error:
	    pass
	audio.tags.add(
	    APIC(
	        encoding=3, # 3 is for utf-8
	        mime='image/jpg', # image/jpeg or image/png
	        type=3, # 3 is for the cover image
	        desc=u'Cover',
	        data=open(artwork_filename).read()
	    )
	)
	audio.save()

def download(url, download_path, silent=True):
	skipper = scdl(link, download_path, silent)
	track_urls = skipper.track_url_dicts
	# downloading media
	return skipper.dl_tracks(track_urls)

if __name__ == "__main__":
	link = sys.argv[1]
	list_of_downloaded_filenames = download(link, '/Users/joeengelman/Music/Soundcloud/', False)
	print
	print "The following files were downloaded successfully:"
	for filename in list_of_downloaded_filenames:
		print "\t{0}".format(filename)
	print "Finished."

