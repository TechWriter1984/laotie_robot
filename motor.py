'''
 # @ Author: XXL
 # @ Create Time: 2023-04-08 22:34:12
 # @ Modified by: Your name
 # @ Modified time: 2023-05-14 15:35:43
 # @ Description:
 '''

import RPi.GPIO as GPIO
import time
import pygame
import pygame.camera
from pygame.locals import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

pwm1 = GPIO.PWM(2, 80)
pwm2 = GPIO.PWM(16, 80)
pwm1.start(0)
pwm2.start(0)

running = True

def turning_right():
    GPIO.output(3, True)
    GPIO.output(4, False)
    GPIO.output(20, True)
    GPIO.output(21, False)
    print('---------------------')
    print('     老铁，右转！    ')
    print('---------------------')

def turning_left():
    GPIO.output(3, False)
    GPIO.output(4, True)
    GPIO.output(20, False)
    GPIO.output(21, True)
    print('---------------------')
    print('     老铁，左转！    ')
    print('---------------------')

def moving_forward():
    GPIO.output(3, True)
    GPIO.output(4, False)
    GPIO.output(20, False)
    GPIO.output(21, True)
    print('---------------------')
    print('     老铁，前进！    ')
    print('---------------------')

def moving_backward():
    GPIO.output(3, False)
    GPIO.output(4, True)
    GPIO.output(20, True)
    GPIO.output(21, False)
    print('---------------------')
    print('     老铁，后退！    ')
    print('---------------------')

def stop():
    GPIO.output(3, False)
    GPIO.output(4, False)
    GPIO.output(20, False)
    GPIO.output(21, False)
    print('---------------------')
    print('     老铁，立正！    ')
    print('---------------------')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pwm1.ChangeDutyCycle(50)
                pwm2.ChangeDutyCycle(50)
                moving_forward()
            elif event.key == pygame.K_DOWN:
                pwm1.ChangeDutyCycle(50)
                pwm2.ChangeDutyCycle(50)
                moving_backward()
            elif event.key == pygame.K_LEFT:
                pwm1.ChangeDutyCycle(50)
                pwm2.ChangeDutyCycle(50)
                turning_left()
            elif event.key == pygame.K_RIGHT:
                pwm1.ChangeDutyCycle(50)
                pwm2.ChangeDutyCycle(50)
                turning_right()
            elif event.key == pygame.K_SPACE:
                stop()
        elif event.type == pygame.KEYUP:
            stop()

pygame.quit()