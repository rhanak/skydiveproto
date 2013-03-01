import pygame
import random

class Ball:
    def __init__(self, radius=50, init_pos=(0, 0), init_speed=[0, 0], color=pygame.Color('red')):
        """
        This function creates a new Ball object. By default, the new Ball
        has a radius of 50 pixels, a starting position of (0,0), a speed
        of (0,0) and a red color.
        """
        # create Surface to hold image for both drawing and erasing the Ball
        self.img = pygame.Surface((radius * 2, radius * 2))
        self.bg = pygame.Surface((radius * 2, radius * 2))
        
        bgColor = pygame.Color('white')
        
        # fill both surfaces with the transparent color
        #transColor = self.img.get_colorkey()
        #self.img.fill(transColor)
        #self.bg.fill(transColor)
        # draw the Ball shape to both the img and the bg surface
        pygame.draw.circle(self.img, color, (radius, radius), radius)
        pygame.draw.circle(self.bg, bgColor, (radius, radius), radius)
        # set the color key for both surfaces
        #self.img.set_colorkey(transColor)
        #self.bg.set_colorkey(transColor)
        # convert both Surfaces for faster bliting to the screen
        self.img.convert()
        self.bg.convert()

        # create rectangle for the Ball image
        # give it the initial position that was passed via init_pos
        self.rect = self.img.get_rect()
        # set the speed of this Ball object
        self.speed = init_speed


    def set_speed(self, new_speed):
        self.speed = new_speed

    def move(self, bounding_rect):
        """
        Moves the Ball object according to self.speed
        Takes a pygame.Rect() object in bounding_rect parameter. When moving,
        checks if the Ball is within the bounds of this rectangle. If not, 
        moves the Ball to correct this situation
        """
        # check if we have a valid bounding_rect. if not, just crash the game
        # after giving an error message
        if not isinstance(bounding_rect, pygame.Rect):
            sys.exit("ERROR: Invalid type for bounding_rect parameter!\n")
        # once we have done sanity checking, continue with moving the Ball
        self.rect.move_ip(self.speed[0], self.speed[1])

        # now, check if the Ball is within the bounds of the bounding_rect
        if bounding_rect.contains(self.rect):
            pass # nothing to do here, as the Ball is within bounds
        else: # if the Ball is outside of bounding_rect
            # first, we find which the direction we are getting out of bounds
            if self.rect.top < bounding_rect.top: 
                # from the TOP side. we move the Ball to the max top first
                self.rect.top = bounding_rect.top
                # then, we check if the Balls current Y velocity will take
                # it out of bounds again. if it will, we inverse the Y velocity
                # by multiplying it with -1
                if (self.rect.top + self.speed[1]) < bounding_rect.top:
                    self.speed[1] *= -1
            elif self.rect.bottom > bounding_rect.bottom:
                # likewise for bottom side
                self.rect.bottom = bounding_rect.bottom
                if (self.rect.bottom + self.speed[1]) > bounding_rect.bottom:
                    self.speed[1] *= -1
            # now, we do the same for the left & right side
            if self.rect.left < bounding_rect.left: 
                self.rect.left = bounding_rect.left
                if (self.rect.left + self.speed[0]) < bounding_rect.left:
                    self.speed[0] *= -1
            elif self.rect.right > bounding_rect.right:
                self.rect.right = bounding_rect.right
                if (self.rect.right + self.speed[0]) > bounding_rect.right:
                    self.speed[0] *= -1

    def erase(self, surface):
        # erase the Ball object from its current location
        surface.blit(self.bg, self.rect)

    def draw(self, surface):
        surface.blit(self.img, self.rect)
      
      
# Collision Detection      
def collision_detect(ball_list, bounding_rect): 
    bList = list(ball_list) 
    for ballA in bList: 
      # remove the current Ball object, as we do not want to test it again 
      bList.remove(ballA) 
      for ballB in bList: 
         # check if the rectangles of the two calls are overlapping 
         # since we are using bounding box collision detection, this is 
         # how we test for a collision 
         if ballA.rect.colliderect(ballB.rect): 
          # inverse the velocity of one of the Ball objects at random 
          b = random.choice([ballA, ballB]) 
          x = b.speed[0] 
          y = b.speed[1] 
          x *= -1 
          y *= -1 
          b.set_speed([x, y]) 
          # now, move the Balls away so they don't collide any more 
          while ballA.rect.colliderect(ballB.rect): 
            ballA.move(bounding_rect) 
            ballB.move(bounding_rect)