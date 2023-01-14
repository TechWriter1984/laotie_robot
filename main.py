# -*- coding: utf-8 -*-
# @Time    :   2023/01/14 18:12:14
# @FileName:   main.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

import smart_camera
import model2

import argparse

import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

SCREEN_SIZE = (640, 480)
CAMERA_SIZE = (400, 300)

screen = pygame.display.set_mode(SCREEN_SIZE, 0)
pygame.display.set_caption("老铁机器人")
cam_list = pygame.camera.list_cameras()
if cam_list:
    cam = pygame.camera.Camera(cam_list[0], CAMERA_SIZE)
    cam.start()
else:
    raise ValueError("未能启动摄像头！请检查摄像头连接是否正常，然后重新启动。")

while True:
    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1, SCREEN_SIZE)
    screen.blit(image1, (0,0))
    pygame.display.update()

    parser = argparse.ArgumentParser()
    parser.add_argument('model_file', type=str)
    args = parser.parse_args()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
          smart_camera.capture_photo()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pwm1.ChangeDutyCycle(50)
            pwm2.ChangeDutyCycle(50)
            moving_forward()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pwm1.ChangeDutyCycle(50)
            pwm2.ChangeDutyCycle(50)
            moving_backward()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            pwm1.ChangeDutyCycle(50)
            pwm2.ChangeDutyCycle(50)
            turning_left()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            pwm1.ChangeDutyCycle(50)
            pwm2.ChangeDutyCycle(50)
            turning_right()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            stop()
