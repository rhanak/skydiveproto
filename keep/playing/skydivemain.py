#!/usr/bin/env python
"""
This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""

# Import Modules
import os, pygame
from pygame.locals import *
from util import *
import pyganim
from animatedsprite import *

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
    pygame.display.set_caption('Skydive demo')
    pygame.mouse.set_visible(0)

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
    #explosion_images = load_sliced_sprites(250, 193, 'skydiver_frontflip_sprite.png')
    #explosion = AnimatedSprite(explosion_images)
    skydiver = pygame.Surface((250,193))
    skydiver_img = load_image('skydiver.gif')[0]
    skydiver.blit(skydiver_img, (0,0))
    skydiver.set_colorkey(skydiver_img.get_at((0,0)))
    
    skydiver_bent1 = pygame.Surface((250,193))
    skydiver_bent1_img = load_image('skydiver_bent1.png')[0]
    skydiver_bent1.blit(skydiver_bent1_img, (0,0))
    skydiver_bent1.set_colorkey(skydiver_bent1_img.get_at((0,0)))
    
    skydiver_bent2 = pygame.Surface((250,193))
    skydiver_bent2_img = load_image('skydive_bent2.gif')[0]
    skydiver_bent2.blit(skydiver_bent2_img, (0,0))
    skydiver_bent2.set_colorkey(skydiver_bent2_img.get_at((0,0)))
    
    skydiver_half = pygame.Surface((250,193))
    skydiver_half_img = load_image('skydive_bent3.gif')[0]
    skydiver_half.blit(skydiver_half_img, (0,0))
    skydiver_half.set_colorkey(skydiver_half_img.get_at((0,0)))
    
    skydiver_upsidedown = pygame.Surface((250,193))
    skydiver_upsidedown_img = load_image('skydiver_upsidedown.gif')[0]
    skydiver_upsidedown.blit(skydiver_upsidedown_img, (0,0))
    skydiver_upsidedown.set_colorkey(skydiver_upsidedown_img.get_at((0,0)))
    
    animObj = pyganim.PygAnimation([(skydiver, 0.1), (skydiver_bent1, 0.1), (skydiver_bent2, 0.1), (skydiver_half, 0.1), (skydiver_upsidedown, 0.1)], loop = False)
    allsprites = pygame.sprite.RenderPlain((fist, chimp))
    animObj.pause()
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

# Game Over


# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()
