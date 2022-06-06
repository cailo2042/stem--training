
import pygame


pygame.init()
screen=pygame.display.set_mode((800,600))

background=pygame.image.load("download.png")
icon=pygame.image.load("icon.png")

pygame.display.set_icon(icon)
pygame.display.set_caption("Space Wars")

while True:
    screen.blit(background,(0,0))
    pygame.display.update()
