# -*- coding: utf-8 -*-
# @Time    :   2023/01/14 18:12:14
# @FileName:   main.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

# from smart_camera import SmartCamera
from chatbot import Chatbot
from chassis import KeyboardChassis
from aiymakerkit import audio
from camera import CameraEye

import sys
import argparse

bot = Chatbot()
ce = CameraEye()
kc = KeyboardChassis()

parser = argparse.ArgumentParser()
parser.add_argument('model_file', type=str)
args = parser.parse_args()

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

    # image1 = cam.get_image()
    # image1 = pygame.transform.scale(image1, (800, 600))
    # screen.blit(image1, (0,0))
    # pygame.display.update()

    # try:
    audio.classify_audio(model=args.model_file, callback=handle_results)
        
    # finally:
    #     cam.stop()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        ce.cam.stop()
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
