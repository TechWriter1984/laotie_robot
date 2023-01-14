import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

SCREEN_SIZE = (640, 480)
CAMERA_SIZE = (400, 300)

screen = pygame.display.set_mode(SCREEN_SIZE, 0)
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], CAMERA_SIZE)
cam.start()

while True:
    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1, SCREEN_SIZE)
    screen.blit(image1,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
            sys.exit()
