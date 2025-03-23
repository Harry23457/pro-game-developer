import pygame
import time

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
    time.sleep(2)
    
    image2 =pygame.image.load("birthday present.jpg")
    font=pygame.font.SysFont("comic sans",40)
    text=font.render("Have a great day",True,"black")
    screen.blit (image2,(0,0))
    screen.blit(text,(100,100))
    pygame.display.update()
    time.sleep(2)

    imag =pygame.image.load("birthday cake.jpg")
    font=pygame.font.SysFont("comic sans",40)
    text=font.render("May your wishes come true",True,"black")
    screen.blit (imag,(0,0))
    screen.blit(text,(50,50))
    pygame.display.update()
    time.sleep(2)


