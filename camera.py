import sys
import pygame
import pygame.camera
from pygame.locals import *
from datetime import datetime
import os
import sys

# pygame.init()
# pygame.camera.init()
# pygame.display.set_caption("老铁机器人")
# pygame.display.update()

class CameraEye():

    # def __init__(self):
        # pygame.init()
        # pygame.camera.init()
        # self.screen = pygame.display.set_mode((800, 600), 0)
        # pygame.display.set_caption("老铁机器人")
        # self.cam_list = pygame.camera.list_cameras()
        # self.cam = pygame.camera.Camera(self.cam_list[0], (640, 480))
        # self.cam.start()
        # self.image1 = self.cam.get_image()
        # self.image1 = pygame.transform.scale(self.image1, (800, 600))
        # self.screen.blit(self.image1,(0,0))
        # pygame.display.update()


    def capture_photo(self):
        timestamp = datetime.now()
        filename = "VOICE_CAM_" + timestamp.strftime("%Y%m%d%H%M%S") + '.jpg'
        filename = os.path.join(self.PICTURE_DIR, filename)
        pygame.image.save(self.image1,"filename")
        print('Saved', filename)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.cam.stop()
            pygame.quit()
            sys.exit()
