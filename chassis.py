# -*- coding: utf-8 -*-
# @Time    :   2022/12/05 17:30:30
# @FileName:   pygame_motor_test.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *

class KeyboardChassis():

    def __init__(self):


        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("老铁1号")

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(4, GPIO.OUT)

        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)

        self.pwm1 = GPIO.PWM(2, 80)
        self.pwm2 = GPIO.PWM(16, 80)
        self.pwm1.start(0)
        self.pwm2.start(0)

        running = True

    def turning_right(self):
        self.pwm1.ChangeDutyCycle(50)
        self.pwm2.ChangeDutyCycle(50)        
        GPIO.output(3, True)
        GPIO.output(4, False)
        GPIO.output(20, True)
        GPIO.output(21, False)
        print('---------------------')
        print('     老铁，右转！    ')
        print('---------------------')

    def turning_left(self):
        self.pwm1.ChangeDutyCycle(50)
        self.pwm2.ChangeDutyCycle(50)        
        GPIO.output(4, True)
        GPIO.output(20, False)
        GPIO.output(21, True)
        print('---------------------')
        print('     老铁，左转！    ')
        print('---------------------')

    def moving_forward(self):
        self.pwm1.ChangeDutyCycle(50)
        self.pwm2.ChangeDutyCycle(50)        
        GPIO.output(4, False)
        GPIO.output(20, False)
        GPIO.output(21, True)
        print('---------------------')
        print('     老铁，前进！    ')
        print('---------------------')

    def moving_backward(self):
        self.pwm1.ChangeDutyCycle(50)
        self.pwm2.ChangeDutyCycle(50)        
        GPIO.output(4, True)
        GPIO.output(20, True)
        GPIO.output(21, False)
        print('---------------------')
        print('     老铁，后退！    ')
        print('---------------------')

    def stop(self):
        self.pwm1.ChangeDutyCycle(50)
        self.pwm2.ChangeDutyCycle(50)        
        GPIO.output(4, False)
        GPIO.output(20, False)
        GPIO.output(21, False)
        print('---------------------')
        print('     老铁，立正！    ')
        print('---------------------')

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
#             pwm1.ChangeDutyCycle(50)
#             pwm2.ChangeDutyCycle(50)
#             moving_forward()
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
#             pwm1.ChangeDutyCycle(50)
#             pwm2.ChangeDutyCycle(50)
#             moving_backward()
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
#             pwm1.ChangeDutyCycle(50)
#             pwm2.ChangeDutyCycle(50)
#             turning_left()
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
#             pwm1.ChangeDutyCycle(50)
#             pwm2.ChangeDutyCycle(50)
#             turning_right()
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             stop()

# pygame.quit()
