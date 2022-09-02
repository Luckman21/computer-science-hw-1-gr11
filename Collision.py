'''
Created on May 23, 2018

@author: Luck
'''
import pygame, sys, time
from random import *
from pygame.locals import *
from pygame.constants import *

fpsClock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption ('Collision')

Red,Blue,Green,White,Black,Orange,Brown = (255,0,0),(0,0,255),(0,255,0),(255,255,255),(0,0,0),(255,127,0),(165,80,80)
c1,c2,shape1,shape2 = 0,3,[],[]
shapes,colours = [shape1,shape2],[Red,Blue,Green,White,Orange,Brown]

def intX(x1,x2):
    '''Controls intersections with x values'''
    
    if x1 == x2 or x2 == x1:   
        return True
            
    else:
        return False

for i in range (0,2):

    r = randint(20,100)
    x,y = r+1,r+1
    shapes[i].append(r)
    shapes[i].append(x)
    shapes[i].append(y)
shapes[0].append(1)
shapes[0].append(1)
shapes[1].append(3)
shapes[1].append(3)
    
shapes[1][1]+=300
shapes[1][2]+=300

Red,Blue,Green,White,Black,Orange,Brown = (255,0,0),(0,0,255),(0,255,0),(255,255,255),(0,0,0),(255,127,0),(165,80,80)

done = False
while not done:
    screen.fill(Black)
     
    for event in pygame.event.get():
            if (event.type == KEYUP) or (event.type == KEYDOWN):
                print event
                if (event.key == K_ESCAPE):
                    done = True
                    sys.exit(0) 
                    pressed = pygame.key.get_pressed()
                    
    for i in range(0,2):
        if i == 0:
            colour = colours[c1]
        else:
            colour = colours[c2]
        
        if shapes[i][1] >= (800-shapes[i][0]) or shapes[i][1] <= (0+shapes[i][0]):
            shapes[i][3]*=-1
        if shapes[i][2] >= (600-shapes[i][0]) or shapes[i][2] <= (0+shapes[i][0]):
            shapes[i][4]*=-1
        
        shapes[i][1]+=shapes[i][3]
        #shapes[i][2]+=shapes[i][4]
        
        print intX(shapes[0][1],shapes[1][1])
        if intX(shapes[0][1],shapes[1][1]) == True:
            
            if (shapes[0][1] > 0 and shapes[1][1] < 0) or (shapes[0][1] < 0 and shapes[1][1] > 0):
                shapes[0][3]*=-1
                shapes[1][3]*=1
                
            if (shapes[0][1] > 0 and shapes[1][1] > 0) or (shapes[0][1] < 0 and shapes[1][1] < 0):
                if shapes[0][1] < shapes[1][1]:
                    shapes[0][3]*=1
                    shapes[1][3]*=-1
                else:
                    shapes[0][3]*=-1
                    shapes[1][3]*=-1
            
            if c1+1 > len(colours)-1:
                c1 = 0 
            else:
                c1+=1
            if c2+1 > len(colours)-1:
                c2 = 0 
            else:
                c2+=1
        
        pygame.draw.rect (screen,colour,(shapes[i][1],shapes[i][2],shapes[i][0],shapes[i][0]))

    pygame.display.update()
    fpsClock.tick(120)
        
        