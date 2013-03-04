import os, pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps = 2):
        pygame.sprite.Sprite.__init__(self)
        self._images = images

        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0

        # Call update to set our first image.
        self.update()

    def update(self):
        if  pygame.time.get_ticks() - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images): self._frame = 0
            self.image = self._images[self._frame]
            self.rect = self.image.get_rect()
            self._last_update =  pygame.time.get_ticks()
            
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos