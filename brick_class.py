import pygame
import random

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)

    def draw(self, screen):
        if self.alive == True:
            pygame.draw.rect(screen, (self.r, self.g, self.b), (self.xpos, self.ypos, 70,20))
        elif self.alive == False:
            pygame.draw.rect(screen, (0, 0, 0), (self.xpos, self.ypos, 50, 20))

    def collide(self, bx: int, by: int) -> bool:
        if self.alive: #hit only alive brick
            if bx >= self.xpos and by > self.ypos and bx <= self.xpos+50 and by < self.ypos+20:
                return True
        return False

                    
    