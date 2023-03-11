# -*- coding: utf-8 -*-
# @Time    :   2023/01/14 18:12:14
# @FileName:   main.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

# turn off alsa output
from ctypes import *
from contextlib import contextmanager
import pyaudio

# from smart_camera import SmartCamera
from chatbot import Chatbot
from chassis import KeyboardChassis
from aiymakerkit import audio

import sys
import argparse

import pygame
from pygame.locals import *
import pygame.camera

# turn off alsa output
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(None)

bot = Chatbot()
# sc = SmartCamera()
kc = KeyboardChassis()

parser = argparse.ArgumentParser()
parser.add_argument('model_file', type=str)
args = parser.parse_args()

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((800, 600), 0)
pygame.display.set_caption("老铁机器人")
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], (640, 480))
cam.start()

# else:
#     raise ValueError("未能启动摄像头！请检查摄像头连接是否正常，然后重新启动。")

def handle_results(label, score):
    print('CALLBACK: ', label, '=>', score)
    bot.greeting()
    if label == '4 laotie':
        bot.greeting()
    # elif label == '2 cheese':
    #     sc.capture_photo()
    elif label == '0 Background Noise':
        bot.dontknow()

    return True

while True:

    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1, (800, 600))
    screen.blit(image1, (0,0))
    pygame.display.update()

    # try:
    audio.classify_audio(model=args.model_file, callback=handle_results)
        
    # finally:
    #     cam.stop()

    with noalsaerr():
        p = pyaudio.PyAudio()
    stream = p.open(format=pyaduio.paFloat32, channels=1, rate=44100, output=1)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        cam.stop()
        pygame.quit()
        sys.exit()
      # elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
      #     sc.capture_photo()
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
          kc.moving_forward()
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
          kc.moving_backward()
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
          kc.turning_left()
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
          kc.turning_right()
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
          kc.stop()
