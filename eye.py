# import necessary libraries
from datetime import datetime
from RPi.GPIO import GPIO
from time import sleep
from pygame import camera
from pygame import image

now = datetime.now()
now = now.strftime("%Y%m%d%H%M%S")
# print(now)