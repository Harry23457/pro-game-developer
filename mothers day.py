import pygame
import time

pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Mother's day card")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    image1 =pygame.transform.scale(pygame.image.load("m1.jpg"),(600,600))
    screen.blit (image1,(0,0))
    pygame.display.update()
    time.sleep(2)

    image2 =pygame.transform.scale(pygame.image.load("m2.jpg"),(600,600))
    screen.blit (image2,(0,0))
    pygame.display.update()
    time.sleep(2)

    image3 =pygame.transform.scale(pygame.image.load("m3.jpg"),(600,600))
    font=pygame.font.SysFont("comic sans",40)
    text=font.render("Hope you have a great day",True,"white")
    screen.blit (image3,(0,0))
    screen.blit(text,(60,530))
    pygame.display.update()
    time.sleep(2)
