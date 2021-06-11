import eel
import random
from datetime import datetime
from audio import audio_processing
from image import image_processing
from video import video_processing

eel.init('web')


@eel.expose
def audio():
    audio_processing()


@eel.expose
def image():
    image_processing()


@eel.expose
def video():
    video_processing()


eel.start('index.html')
