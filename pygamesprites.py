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
        self.rect.y=random.randint(-200,20)
    def update(self):
        self.rect.y+=1
        if self.rect.y>400:
            self.reset_pos()

class r(b):
    def update(self):
        pos=pygame.mouse.get_pos()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
blacklist=pygame.sprite.Group()
allsprites=pygame.sprite.Group()
for i in range(50):
    black=b("black")
    black.rect.x=random.randint(0,700)
    black.rect.y=random.randint(0,400)
    blacklist.add(black)
    allsprites.add(black)
red=r("red")
allsprites.add(red)

clock=pygame.time.Clock()

score=0

    
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("white")
    allsprites.update()
    cl=pygame.sprite.spritecollide(red,blacklist,False)
    for i in cl:
        i.reset_pos()
        score+=1
        print(score)
        


   
    allsprites.draw(screen)
    clock.tick(20)
    pygame.display.update()
    








        


