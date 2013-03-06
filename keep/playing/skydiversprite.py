from util import *
import pygame
import pyganim

def skydiver_anim():
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
  return animObj