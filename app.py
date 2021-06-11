import eel
import random
from datetime import datetime
from audio import audio_processing
from image import image_processing

eel.init('web')


@eel.expose
def audio():
    audio_processing()


@eel.expose
def image():
    image_processing()


@eel.expose
def get_date():
    eel.prompt_alerts(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


@eel.expose
def get_ip():
    eel.prompt_alerts('127.0.0.1')


eel.start('index.html')
