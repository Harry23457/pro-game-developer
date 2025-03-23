import pygame

pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Rocket in space")

class rocket (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("ship.png")
        self.image=pygame.transform.scale(self.image,(75,116))
        self.rect=self.image.get_rect()
    def draw (self):
        screen.blit(self.image,(100,100))
    def update(self,key):
        if key[pygame.K_UP]:
            self.rect.move_ip(0,-5)
r1=rocket()
bg=pygame.image.load("space.png")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    key=pygame.key.get_pressed()
    r1.update(key)
    screen.blit(bg,(0,0))
    r1.draw()

    pygame.display.update()
