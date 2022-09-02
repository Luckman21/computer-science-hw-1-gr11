'''
Created on Apr 18, 2018

@author: Luck
'''
import pygame, sys, time
from pygame.locals import *
from pygame.constants import *

fpsClock = pygame.time.Clock()
pygame.init()

# set the screen
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption ('Windows Defender - Virus Detected')

Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)
White = (255,255,255)

screen.fill(Green)

pygame.draw.circle (screen, Blue,(170,170), 100, 59)
pygame.draw.rect (screen, Red,(200,220,40,200))

pygame.display.update()
fpsClock.tick(30)

done = False
while not done:
    for event in pygame.event.get():
        if (event.type == KEYUP) or (event.type == KEYDOWN):
            print event
            if (event.key == K_ESCAPE):
                done = True
sys.exit(0)             

pygame.draw.circle (screen, Blue,(x,y), r, 0)
pygame.draw.rect (screen, Red,(x,y,w,h))



