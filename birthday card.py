import pygame

pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("birthday")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    image1 =pygame.image.load("birthday card.jpg")
    font=pygame.font.SysFont("comic sans",40)
    text=font.render("Happy Birthday",True,"black")
    screen.blit (image1,(0,0))
    screen.blit(text,(150,200))
    pygame.display.update()

