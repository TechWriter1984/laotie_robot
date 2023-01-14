import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((800, 600), 0)
pygame.display.set_caption("老铁机器人")
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0], (640, 480))
cam.start()

while True:
    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1, (800, 600))
    screen.blit(image1,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
            sys.exit()
