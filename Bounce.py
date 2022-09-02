'''
Created on May 23, 2018

@author: Luck
'''
import pygame, sys, time
from random import randint
from pygame.locals import *
from pygame.constants import *

fpsClock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption ('Bounce')

r = randint(1,100)
x,y,xd,yd = r+1,r+1,randint(1,5),randint(1,5)

Red,Blue,Green,White,Black,Orange,Brown = (255,0,0),(0,0,255),(0,255,0),(255,255,255),(0,0,0),(255,127,0),(165,80,80)

done = False
while not done:
    screen.fill(Black)
    fpsClock.tick(60)
    
    pygame.draw.circle (screen, Red,(x,y), r, 0)
    
    if x >= (800-r) or x <= (0+r):
        xd*=-1
    if y >= (600-r) or y <= (0+r):
        yd*=-1
    
    x+=xd
    y+=yd
    
    pressed = pygame.key.get_pressed()
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if (event.type == KEYUP) or (event.type == KEYDOWN):
            print event
            if (event.key == K_ESCAPE):
                done = True
                sys.exit(0) 
    