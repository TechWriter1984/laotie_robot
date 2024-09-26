# Chassis

This page describes the chassis of Laotie. 

## Hardware

The chassis is composed by the following hardware:

| QTY |                                             image                                             |     Component      |        Link         |          Est. Cost          |
| :-: | :-------------------------------------------------------------------------------------------: | :----------------: | :-----------------: | :-------------------------: |
|  1  | ![Tank Caterpillar](https://cbu01.alicdn.com/img/ibank/2018/137/022/8875220731_806910891.jpg) |  tank chassis 4WD  | [Link](URL_ADDRESS) |             $20             |
|  1  |    ![L298N](https://th.bing.com/th/id/OIP.r56hYlacKitBOO4nVdP0eAHaHa?rs=1&pid=ImgDetMain)     | L298N motor driver | [Link](URL_ADDRESS) |             $10             |
|  2  |   ![DC motor](https://th.bing.com/th/id/OIP.ZkRZOIoGP3DU2NCCo-BvDQHaHa?rs=1&pid=ImgDetMain)   |     DC motors      | [Link](URL_ADDRESS) | comes with the tank chassis |

## Software

> [!NOTE]
> The source code below is only a demo of the motor_control.py module. It is not the final version.

Laotie's chassis is a Python implementation using the [jetson.gpio](https://github.com/NVIDIA/jetson-gpio) library to manipulate the 40 GPIO pins on Jetson Nano.

### Source Code

The source code is located in the `src` directory. The `motor_control.py` module is responsible for controlling the motors.

#### The MotorControl Class

```python
# This is only a demo of the motor_control.py module

import Jetson.GPIO as GPIO
from hardware.l298n_driver import set_motor_speed_and_direction

class MotorControl:
    def __init__(self):
        # 设置电机引脚
        self.IN1 = [pin1, pin2]  # 根据实际情况设置
        self.IN2 = [pin3, pin4]
        self.ENA = pin5
        self.ENB = pin6

        # 设置 GPIO 模式为 BOARD
        GPIO.setmode(GPIO.BOARD)

        # 设置电机引脚为输出模式
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)

    def set_speed(self, left_speed, right_speed):
        set_motor_speed_and_direction(left_speed, right_speed, self.IN1, self.IN2, self.ENA, self.ENB)

    def stop(self):
        self.set_speed(0, 0)

    def cleanup(self):
        # 停止电机控制并清理 GPIO 资源
        self.stop()
        GPIO.cleanup()
```

#### How to Use

```python
from control.motor_control import MotorControl

motor_control = MotorControl()

# 设置电机速度
motor_control.set_speed(50, 50)  # 设置左右电机速度为 50%

# 停止电机
motor_control.stop()

# 清理资源
motor_control.cleanup()
```