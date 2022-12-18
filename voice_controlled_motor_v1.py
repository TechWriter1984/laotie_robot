# -*- coding: utf-8 -*-
# @Time    :   2022/12/10 22:50:15
# @FileName:   voice_controlled_motor.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

from picamera import PiCamera
from aiymakerkit import audio
import keyboard_controlled_motor

from datetime import datetime
import os

# Mind that this path here must be the one in your Raspbian OS
PICTURE_DIR = os.path.join((os.path.expanduser('~')), 'Pictures')
IMAGE_SIZE = (640, 480)
camera = picamera.PiCamera(resolution = IMAGE_SIZE)

def handle_results(label, score):
    if label == 'Stop':
        return False
    elif label == 'Cheese':
        capture_photo()    
    return True

def capture_photo():
    timestamp = datetime.now()
    filename = "laotie_" + timestamp.strftime("%Y%m%d%H%M%S") + ".png"
    filename = os.path.join(PICTURE_DIR, filename)
    camera.capture(filename)
    print('Saved', filename)

try:
    audio.classify_audio(model_file = args.model, callback = handle_results)
finally:
    camera.close()

def main():
    pass

if __name__ == '__main__':
    main()