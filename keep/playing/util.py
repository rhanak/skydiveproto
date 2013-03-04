import os
import pygame

from pygame.locals import *
from pygame.compat import geterror
    
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

#functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def load_sliced_sprites(w, h, filename):
    '''
    Specs :
      Master can be any height.
      Sprites frames width must be the same width
      Master width must be len(frames)*frame.width
    Assuming you ressources directory is named "ressources"
    '''
    images = []
    master_image = pygame.image.load(os.path.join(data_dir, filename)).convert_alpha()
    
    master_width, master_height = master_image.get_size()
    for i in xrange(int(master_width/w)):
      # set the trasparent color
      image = master_image.subsurface((i*w,0,w,h))
      colorkey = image.get_at((2,2))
      image.set_colorkey(colorkey)
      images.append(image)
    return images
