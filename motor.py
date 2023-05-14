'''
 # @ Author: XXL
 # @ Create Time: 2023-04-08 22:34:12
 # @ Modified by: ChatGPT
 # @ Modified time: 2023-05-14 15:35:43
 # @ Description:
 '''

import RPi.GPIO as GPIO
import time
import pygame
import pygame.camera
from pygame.locals import *
import threading

pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("老铁机器人")
cam_list = pygame.camera.list_cameras()
if not cam_list:
    raise ValueError("没检测到摄像头！")
cam = pygame.camera.Camera(cam_list[0], (800, 600))
cam.start()

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

movement_map = {
    pygame.K_UP: (40, 40, True, False, False, True, '前进'),
    pygame.K_DOWN: (40, 40, False, True, True, False, '后退'),
    pygame.K_LEFT: (40, 40, False, True, False, True, '左转'),
    pygame.K_RIGHT: (40, 40, True, False, True, False, '右转'),
    pygame.K_SPACE: (0, 0, False, False, False, False, '立正')
}

def set_motor(pwm1_duty_cycle, pwm2_duty_cycle, gpio_3, gpio_4, gpio_20, gpio_21, message):
    GPIO.output(3, gpio_3)
    GPIO.output(4, gpio_4)
    GPIO.output(20, gpio_20)
    GPIO.output(21, gpio_21)
    pwm1.ChangeDutyCycle(pwm1_duty_cycle)
    pwm2.ChangeDutyCycle(pwm2_duty_cycle)
    print('---------------------')
    print(f'     老铁，{message}！    ')
    print('---------------------')

def process_movement(event):
    if event.key in movement_map:
        pwm1_duty_cycle, pwm2_duty_cycle, gpio_3, gpio_4, gpio_20, gpio_21, message = movement_map[event.key]
        set_motor(pwm1_duty_cycle, pwm2_duty_cycle, gpio_3, gpio_4, gpio_20, gpio_21, message)
    else:
        set_motor(0, 0, False, False, False, False, '立正')

def camera_loop():
    while running:
        image1 = cam.get_image()
        image1 = pygame.transform.scale(image1, (800, 600))
        screen.blit(image1, (0, 0))
        pygame.display.update()

def keyboard_loop():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                t = threading.Thread(target=process_movement, args=(event,))
                t.start()
            elif event.type == pygame.KEYUP:
                set_motor(0, 0, False, False, False, False, '立正')

running = True

t1 = threading.Thread(target=camera_loop)
t1.start()

t2 = threading.Thread(target=keyboard_loop)
t2.start()

t2.join()
t1.join()

