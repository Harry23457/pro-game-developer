import pygame
import random
pygame.init()
screen=pygame.display.set_mode((700,400))
class b(pygame.sprite.Sprite):
    def __init__(self,clr):
        super().__init__()
        self.image=pygame.Surface((20,15))
        self.image.fill(clr)
        self.rect=self.image.get_rect()
    def reset_pos(self):
        self.rect.x=random.randint(20,680)
        self.rect.y=random.randint(-200,-20)
