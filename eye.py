# import necessary libraries
import os.path
from datetime import datetime
from time import sleep

# from pygame import camera
# from pygame import image

from picamera import PiCamera
from RPi.GPIO import GPIO
from aiymakerkit import vision

timestamp = datetime.now()
filename = "LaoTie_" + timestamp.strftime("%Y%m%d%H%M%S") + '.png'
filename = os.path.join(PICTURE_DIR, filename)
vision.save_frame(filename, frame)
