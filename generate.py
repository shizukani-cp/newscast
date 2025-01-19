import os, glob, json
from logging import getLogger, basicConfig, INFO
import feedparser
import audio

basicConfig(level=INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = getLogger(__name__)

with open("public/urls.json", encoding="utf-8") as f:
    url_data = json.loads(f.read())

for f in glob.glob("public/*.mp3"): os.remove(f)

for url in url_data:
    logger.info(url)
    read_text = ""
    d = feedparser.parse(url["url"])
    for entry in d.entries:
        read_text += entry.summary
        read_text += "\n"
    audio.generate(read_text)
    os.rename("out.mp3", f"public/{url['fname']}.mp3")

