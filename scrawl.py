import scdl
from scdl import colors
from bs4 import BeautifulSoup
import urllib

DOWNLOAD_PATH = './Soundcloud/Crawler/'

future_urls = []
visited_urls = []
downloaded_filenames = []

initial_url = raw_input("Enter initial URL: ")
future_urls.append(initial_url)

num_pages = input("How many pages should Scrawl traverse? ")

for page in range(num_pages):
	url = future_urls.pop()
	if url not in visited_urls:
		visited_urls.append(url)
		downloaded_filenames += scdl.download(url, DOWNLOAD_PATH, silent=False)
		soup = BeautifulSoup(urllib.urlopen(url + "/recommended"))
		for related in soup.find_all(itemprop="url"):
			future_urls.append("https://soundcloud.com" + related['href'])

print
print colors.HEADER + "The following files were downloaded successfully:" + colors.END
for i, filename in enumerate(downloaded_filenames):
	print "\t" + colors.HEADER + str(i+1) + ". " + colors.END + colors.OKBLUE + " {0}".format(filename[len(DOWNLOAD_PATH):]) + colors.END
print colors.OKGREEN + "Finished." + colors.END


