import pygame

class MySprite():

  def __init__(self, image, x, maxX, y, maxY):

    self.x = x
    self.y = y
    self.image = image
    self.rectangle = pygame.Rect(
      x, y, image.get_width(), image.get_height())
    self.maxX = maxX - image.get_width()
    self.maxY = maxY - image.get_height()
  
  def GetPosition(self):
    return (self.x, self.y)

  def AddX(self, x):
    self.x = self.x + x

  def SubX(self, x):
    self.x = self.x - x

  def AddY(self, y):
    self.y = self.y + y

  def SubY(self, y):
    self.y = self.y - y
    
  def Update(self, scr=None):
    if self.x < 0:
      self.x = self.maxX

    if self.x > self.maxX:
      self.x = 0

    if self.y < 0:
      self.y = self.maxY

    if self.y > self.maxY:
      self.y = 0

    self.rectangle.move_ip(self.x, self.y)

    if scr != None:
      scr.blit(self.image, self.GetPosition())
      