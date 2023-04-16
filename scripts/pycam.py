from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (800, 600)
camera.start_preview()
sleep(5)
camera.capture("1.jpg")