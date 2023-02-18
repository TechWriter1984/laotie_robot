# -*- coding: utf-8 -*-
# @Time    :   2022/12/06 20:58:54
# @FileName:   smart_camera.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

from aiymakerkit import audio
import argparse
import chatbot

from picamera import PiCamera
from datetime import datetime
import os

class SmartCamera:

    def __init__(self):

        self.PICTURE_DIR = os.path.join(os.path.expanduser('~'), 'Pictures')
        self.IMAGE_SIZE = (640, 480)
        self.camera=PiCamera(resolution = self.IMAGE_SIZE)

    def capture_photo(self):
        timestamp = datetime.now()
        filename = "VOICE_CAM_" + timestamp.strftime("%Y%m%d%H%M%S") + '.jpg'
        filename = os.path.join(self.PICTURE_DIR, filename)
        self.camera.capture(filename)
        print('Saved', filename)

# def handle_results(label, score):
#     print('CALLBACK: ', label, '=>', score)
#     chatbot.greeting()
#     if label == '4 laotie':
#         chatbot.greeting()
#     elif label == '2 cheese':
#         capture_photo()
#     elif label == '0 Background Noise':
#         chatbot.dontknow()
#     return True

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('model_file', type=str)
#     args = parser.parse_args()

#     try:
#         audio.classify_audio(model=args.model_file, callback=handle_results)
        
#     finally:
#         camera.close()

# if __name__ == '__main__':
#     main()
