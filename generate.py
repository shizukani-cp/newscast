import os
import feedparser
import audio

with open("urls.txt") as f:
    urls = f.readlines()

read_text = ""

for url in urls:
    d = feedparser.parse(url)
    for entry in d.entries:
        read_text += entry.summary
        read_text += "\n"
    print(url)

audio.generate(read_text)

os.rename("out.mp3", "cast.mp3")

