from scdl import download
from scdl import colors
from bs4 import BeautifulSoup
import urllib
import os

DOWNLOAD_PATH = os.path.expanduser('~/Music/Soundcloud/Crawler/')	# choose where to download tracks

future_urls = []			# a queue for URLs to visit in the future
visited_urls = []			# a list of URLs already visited
downloaded_filenames = []	# a list of filenames where downloaded tracks have been stored

# begin the search at some user-specified URL
initial_url = raw_input("Enter initial URL: ")
future_urls.append(initial_url)

# num_pages determines how many pages the search will visit, but not necessarily
#	the number of tracks which will be downloaded (duplicate tracks will only be
#	downloaded once, although their pages may be visited many times)
num_pages = input("How many pages should Scrawl traverse? ")

for page in range(num_pages):
	# pull the next URL off the queue
	url = future_urls.pop()
	if url not in visited_urls:		# make sure this track has not been downloaded already
		visited_urls.append(url)	# mark URL as visited so it is avoided in the future
		downloaded_filenames += download(url, DOWNLOAD_PATH, silent=False)	# download track
		soup = BeautifulSoup(urllib.urlopen(url + "/recommended"))	# find recommended tracks
		for related in soup.find_all(itemprop="url"):	# look for links to other tracks
			future_urls.append("https://soundcloud.com" + related['href'])	# add recommended
																			#  tracks to queue

print
print colors.HEADER + "The following files were downloaded successfully:" + colors.END
for i, filename in enumerate(downloaded_filenames):		# print all files downloaded
	print "\t" + colors.HEADER + str(i+1) + ". " + colors.END + colors.OKBLUE + " {0}".format(filename[len(DOWNLOAD_PATH):]) + colors.END
print colors.OKGREEN + "Finished." + colors.END


