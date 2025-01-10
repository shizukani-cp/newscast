import os
from logging import getLogger, basicConfig, INFO
import feedparser
import audio

basicConfig(level=INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = getLogger(__name__)

with open("urls.txt") as f:
    urls = f.readlines()

read_text = ""

for url in urls:
    d = feedparser.parse(url)
    for entry in d.entries:
        read_text += entry.summary
        read_text += "\n"
    logger.info(url)

audio.generate(read_text)

os.rename("out.mp3", "cast.mp3")

