# -*- coding: utf-8 -*-
# @Time    :   2023/05/21 21:41:41
# @FileName:   chassis.py
# @Author  :   TechWriter1984
# @E-mail  :   oopswow@126.com

import RPi.GPIO as GPIO
import time
import pygame
import pygame.camera
from pygame.locals import *
import threading

class RobotController:
    def __init__(self):
        pygame.init()
        pygame.camera.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        pygame.display.set_caption("老铁机器人")
        cam_list = pygame.camera.list_cameras()
        if not cam_list:
            raise ValueError("没检测到摄像头！")
        self.cam = pygame.camera.Camera(cam_list[0], (800, 600))
        self.cam.start()

        self.camera_lock = threading.Lock()

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

        self.movement_map = {
            pygame.K_UP: (40, 40, True, False, False, True, '前进'),
            pygame.K_DOWN: (40, 40, False, True, True, False, '后退'),
            pygame.K_LEFT: (40, 40, False, True, False, True, '左转'),
            pygame.K_RIGHT: (40, 40, True, False, True, False, '右转'),
            pygame.K_SPACE: (0, 0, False, False, False, False, '立正')
        }

        self.running = True
        self.t1 = threading.Thread(target=self.camera_loop)
        self.t1.setDaemon(True)
        self.t2 = threading.Thread(target=self.keyboard_loop)

    def set_motor(self, pwm1_duty_cycle, pwm2_duty_cycle, gpio_3, gpio_4, gpio_20, gpio_21, message):
        GPIO.output(3, gpio_3)
        GPIO.output(4, gpio_4)
        GPIO.output(20, gpio_20)
        GPIO.output(21, gpio_21)
        self.pwm1.ChangeDutyCycle(pwm1_duty_cycle)
        self.pwm2.ChangeDutyCycle(pwm2_duty_cycle)
        print('---------------------')
        print(f'     老铁，{message}！    ')
        print('---------------------')

    def process_movement(self, event):
        if event.key in self.movement_map:
            pwm1_duty_cycle, pwm2_duty_cycle, gpio_3, gpio_4, gpio_20, gpio_21, message = self.movement_map[event.key]
            self.set_motor(pwm1_duty_cycle, pwm2_duty_cycle, gpio_3, gpio_4, gpio_20, gpio_21, message)
        else:
            self.set_motor(0, 0, False, False, False, False, '立正')

    def camera_loop(self):
        while self.running:
            self.camera_lock.acquire()
            image1 = self.cam.get_image()
            image1 = pygame.transform.scale(image1, (800, 600))
            self.screen.blit(image1, (0, 0))
            pygame.display.update()
            self.camera_lock.release()

    def keyboard_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    t = threading.Thread(target=self.process_movement, args=(event,))
                    t.start()
                elif event.type == pygame.KEYUP:
                    self.set_motor(0, 0, False, False, False, False, '立正')

    def run(self):
        self.t1.start()
        self.t2.start()

        self.t2.join()
        self.t1.join()

robot = RobotController()
robot.run()
