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
import pygame
import pygame.camera
from pygame.locals import *
# These lines of code are importing the necessary modules and functions from the Pygame library for
# capturing images from a camera. `pygame` is the main module for Pygame, `pygame.camera` is a module
# for accessing cameras, and `from pygame.locals import *` is importing constants and functions from
# the Pygame.locals module, which includes event types and key constants.
# import pygame
# import pygame.camera
# from pygame.locals import *

pygame.init()
pygame.camera.init()

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
    elif label == '2 cheese':
        ce.capture_photo()
    elif label == '0 Background Noise':
        bot.dontknow()
    elif label == '3 forward':
        kc.pwm1.ChangeDutyCycle(50)
        kc.pwm2.ChangeDutyCycle(50)
        kc.moving_forward()
    elif label == '1 backward':
        kc.pwm1.ChangeDutyCycle(50)
        kc.pwm2.ChangeDutyCycle(50)
        kc.moving_backward()
    elif label == '5 left':
        kc.pwm1.ChangeDutyCycle(50)
        kc.pwm2.ChangeDutyCycle(50)
        kc.turning_left
    elif label == '6 right':
        kc.pwm1.ChangeDutyCycle(50)
        kc.pwm2.ChangeDutyCycle(50)
        kc.turning_right()
    elif label == '7 stop':
        kc.stop()

    return True

while True:

    image1 = ce.cam.get_image()
    image1 = pygame.transform.scale(image1, (640,480))
    ce.screen.blit(image1, (0, 0))
    pygame.display.update()
    

    # try:
    audio.classify_audio(model=args.model_file, callback=handle_results)
        
    # finally:
    #     cam.stop()

    # for event in pygame.event.get():
    #   if event.type == pygame.QUIT:
    #     ce.cam.stop()
    #     pygame.quit()
    #     sys.exit()
    #   # elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
    #   #     sc.capture_photo()
    #   elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
    #       kc.pwm1.ChangeDutyCycle(50)
    #       kc.pwm2.ChangeDutyCycle(50)
    #       kc.moving_forward()
    #   elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
    #       kc.pwm1.ChangeDutyCycle(50)
    #       kc.pwm2.ChangeDutyCycle(50)        
    #       kc.moving_backward()
    #   elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
    #       kc.pwm1.ChangeDutyCycle(50)
    #       kc.pwm2.ChangeDutyCycle(50)      
    #       kc.turning_left()
    #   elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    #       kc.pwm1.ChangeDutyCycle(50)
    #       kc.pwm2.ChangeDutyCycle(50)
    #       kc.turning_right()
    #   elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #       kc.stop()
