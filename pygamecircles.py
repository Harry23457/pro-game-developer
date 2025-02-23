import pygame
pygame.init()
screen=pygame.display.set_mode([500,500])
screen.fill("white")
class mycircle():
    def __init__(self,color,pos,radius,width=0):
        self.color=color
        self.pos=pos
        self.radius=radius
        self.width=width
        self.screen=screen
    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.width)
    def growcircle(self,x):
        self.radius+=x
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.width)

c1=mycircle("red",(250,250),50,15)
c2=mycircle("yellow",(250,250),90,15)
c3=mycircle("red",(250,250),120,15)
c4=mycircle("blue",(250,250),140,15)
c5=mycircle("orange",(250,250),200,15)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            c1.draw()
            c2.draw()
            c3.draw()
            c4.draw()
            c5.draw()
            pygame.display.update()

        
