from pytube import YouTube
from sys import argv

#the link argument- take all of the things that u input into command line when u run this program/ while argv[0] is the name of the 
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('/Users/lailazoabi/Desktop/DV/')

#run with python3 ytDownloader.py "LINK"