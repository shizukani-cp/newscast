import os, sys, shutil, time
from logging import getLogger
import gtts
from pydub import AudioSegment
from langdetect import detect

logger = getLogger(__name__)

def _main(sentences, wait_time=1):
    splitted_sentences = sentences.splitlines()
    if len(splitted_sentences) == 0:
        logger.fatal("入力がありません")
    for n, s in enumerate(splitted_sentences):
        logger.info(f"read: {n} / {len(splitted_sentences)}")
        gtts.gTTS(s, lang=detect(s)).save(f"tmp/{n}.mp3")
        time.sleep(wait_time)

    data = AudioSegment.from_file("tmp/0.mp3")
    logger.info(f"join: 1 / {n}")
    for f in range(1, n):
        data += AudioSegment.from_file(f"tmp/{f}.mp3")
        logger.info(f"join: {f+1} / {n}")

    data.export("out.mp3", format="mp3")

def generate(text):
    if os.path.exists("tmp"):
        shutil.rmtree("tmp")
    os.makedirs("tmp", exist_ok=True)
    _main(text)
    shutil.rmtree("tmp")
