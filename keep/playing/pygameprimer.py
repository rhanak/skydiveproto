#Import and Init
import pygame
from pygame.locals import *
from mysprite import MySprite
from util import *

pygame.init()

#Set Up the Window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sprite Test!")

#SOTC Green Background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

#Load and Convert the SOTC Logo
sotcLogo = load_image("truck.jpeg")

#Position variables
lx = 100
ly = 100
speed = 3

#Right and Bottom Bounds for Game Entities
rightBound = screen.get_width() - sotcLogo.get_width()
bottomBound = screen.get_height() - sotcLogo.get_height()

#Initialize sprites
spriteCanImg = load_image("sprite.gif")
transColor = spriteCanImg.get_at((1,1))
spriteCanImg.set_colorkey(transColor)

sprite = MySprite(spriteCanImg, 0, screen.get_width(), 0, screen.get_height())

boom_sound = load_sound('boom.wav')

#Clock and Loop Variables
framerate = pygame.time.Clock()
GameGo = True

#The Main Loop
while GameGo:

  #Tick the Clock
  framerate.tick(60)
  
  #Keyborad Keypress Events, Movement
  if pygame.key.get_pressed()[K_UP]:
    ly = ly - speed
  if pygame.key.get_pressed()[K_DOWN]:
    ly = ly + speed
  if pygame.key.get_pressed()[K_LEFT]:
    lx = lx - speed
  if pygame.key.get_pressed()[K_RIGHT]:
    lx = lx + speed

  #Test for Out-of-Bounds
  if lx > rightBound:
    lx = rightBound
    boom_sound.play()
  if lx < 0:
    lx = 0
    boom_sound.play()
  if ly > bottomBound:
    ly = bottomBound
    boom_sound.play()
  if ly < 0:
    ly = 0
    boom_sound.play()
  
  #Blit our Images
  screen.blit(background, (0, 0))
  screen.blit(sotcLogo, (lx, ly))
  
  #Update our Sprites
  sprite.AddX(3)
  sprite.AddY(3)
  sprite.Update(screen)
  
  # Collision detection
  
  #Update the Display
  pygame.display.update()

  #Handle a Close Event
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      GameGo = False