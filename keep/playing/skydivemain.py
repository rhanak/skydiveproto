#!/usr/bin/env python
"""
Skydive Demo Randy Hanak
"""

# Import Modules
import sys
sys.path.insert(0, 'dumbmenu')
import dumbmenu as dm

import os, pygame
from pygame.locals import *
from util import *
import pyganim
from skydiversprite import *

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

# classes for our game objects
class Fist(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('skydiver.gif', -1)
        self.punching = 0

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        "returns true if the fist collides with the target"
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        "called to pull the fist back"
        self.punching = 0


class Chimp(pygame.sprite.Sprite):
    """moves a monkey critter across the screen. it can spin the
       monkey when it is punched."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 4
        self.dizzy = 0

    def update(self):
        "walk or spin, depending on the monkeys state"
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        "move the monkey across the screen, and turn at the ends"
        newpos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or \
            self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        "spin the monkey image"
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        "this will cause the monkey to start spinning"
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.key.set_repeat(500,30)
    pygame.display.set_caption('Skydive demo')
    pygame.mouse.set_visible(0)

    red   = 255,  0,  0
    green =   0,255,  0
    choose = dm.dumbmenu(screen, [
                            'Start Game',
                            'Options',
                            'Manual',
                            'Show Highscore',
                            'Quit Game'], 64,64,None,32,1.4,green,red)

    if choose == 0:
        print "You choose 'Start Game'."
    elif choose == 1:
        print "You choose 'Options'."
    elif choose == 2:
        print "You choose 'Manual'."
    elif choose == 3:
        print "You choose 'Show Highscore'."
    elif choose == 4:
        pygame.quit()
        exit()

    # Create The Backgound
    background, background_rect = load_image('mount_everest.jpg', -1)
    
    # Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Pummel The Chimp, And Win ", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()
    whiff_sound = load_sound('whiff.wav')
    punch_sound = load_sound('punch.wav')
    chimp = Chimp()
    fist = Fist()
    
    # Create our skydiver animation
    animObj = skydiver_anim()
    animObj.pause()
    # Create the group of sprites
    allsprites = pygame.sprite.RenderPlain((fist, chimp))
    
    # Main Loop
    going = True
    while going:
        clock.tick(60)

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_UP:
                animObj.play()
            elif event.type == MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play() #punch
                    chimp.punched()
                else:
                    whiff_sound.play() #miss
            elif event.type == MOUSEBUTTONUP:
                fist.unpunch()
        
        allsprites.update()

        #Draw Everything
        screen.blit(background, (0, 0))
        animObj.blit(screen, (200, 200))
        allsprites.draw(screen)
        pygame.display.flip()
        
        if animObj._state ==  pyganim.STOPPED:
            animObj.pause()

    pygame.quit()

# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()
