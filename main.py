import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Race of the Races")
DISPLAYSURF = pygame.display.set_mode((1000,500))
DISPLAYSURF.fill('darkgreen')
pygame.draw.circle(DISPLAYSURF, pygame.Color('white'), (200,50), 30)
FPS = pygame.time.Clock()
FPS.tick(60)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

