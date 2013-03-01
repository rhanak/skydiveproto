import pygame
import random

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
black = [0,0,0]
UP = [0,-1]
DOWN = [0,1]
LEFT = [-1,0]
RIGHT = [1,0]
NOTMOVING = [0,0]
#constants end
#classes
class collidable:
    x = 0
    y = 0
    w = 0
    h = 0
    rect = pygame.Rect(x,y,w,h)
    color = [0,0,0]
    def __init__(self,x,y,w,h,color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect = pygame.Rect(x,y,w,h)
    def draw(self):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.w,self.h],6)

class player:
    x = 0
    y = 0
    speed = 0
    rect = pygame.Rect(x,y,20,20)
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(self.x,self.y,20,20)
    def draw(self):
        if player_moving==LEFT:
                pygame.draw.polygon(screen,black,[(self.x-10,self.y),(self.x+10,self.y-10),(self.x+10,self.y+10)])
        elif player_moving==RIGHT:
            pygame.draw.polygon(screen,black,[(self.x+10,self.y),(self.x-10,self.y-10),(self.x-10,self.y+10)])
        elif player_moving==UP:
            pygame.draw.polygon(screen,black,[(self.x,self.y-10),(self.x+10,self.y+10),(self.x-10,self.y+10)])
        elif player_moving==DOWN:
            pygame.draw.polygon(screen,black,[(self.x,self.y+10),(self.x+10,self.y-10),(self.x-10,self.y-10)])
        else:
            pygame.draw.rect(screen,black,pygame.Rect(self.x-10,self.y-10,20,20),6)
    def setpos(self,x,y):
        self.x = x
        self.y = y
    def move(self,direction):
        self.x = self.x + direction[0]*self.speed
        self.y = self.y + direction[1]*self.speed
        self.rect = pygame.Rect(self.x,self.y,20,20)
#classes end

#globals
pygame.init()
screenSize = [800,600]
screenBGColor = white
screen=pygame.display.set_mode(screenSize)
pygame.display.set_caption("Move the Block")
player = player(screenSize[0]/2,screenSize[1]/2,9)
collidables = []
clock=pygame.time.Clock()
for i in range(10):
    collidables.append(collidable(random.randrange(0,screenSize[0]),random.randrange(0,screenSize[1]),random.randrange(10,200),random.randrange(10,200),blue))

running = True
#globals end
player_moving = NOTMOVING
#functions
def render():
    screen.fill(screenBGColor)
    clock.tick(60)
    player.draw()
    for c in collidables:
        c.draw()
    pygame.display.flip()
def tick(player_moving):                                           #----------------HERE
    for c in collidables:
        if player.rect.colliderect(c.rect):
            player_moving = NOTMOVING
            print("hit"+str(c.rect)+" with "+str(player.rect))
    player.move(player_moving)

#functions end

#main loop
while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_moving = LEFT
            if event.key==pygame.K_RIGHT:
                player_moving = RIGHT
            if event.key==pygame.K_UP:
                player_moving = UP
            if event.key==pygame.K_DOWN:
                player_moving = DOWN
        else:
            player_moving = NOTMOVING
    tick(player_moving)
    render()
#main loop end

pygame.quit()
