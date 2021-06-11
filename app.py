import eel
import random
from datetime import datetime
from audio import audio_processing
from image import image_processing
from video import video_processing
import wx

eel.init('web')

file_path = ''

@eel.expose
def pythonFunction(wildcard="*"):
    global file_path
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    file_path = path

@eel.expose
def audio():
    audio_processing()


@eel.expose
def image():
    global file_path
    image_processing(file_path)



@eel.expose
def video():
    global file_path
    video_processing(file_path)


eel.start('index.html')
