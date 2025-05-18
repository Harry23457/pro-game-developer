import pygame
pygame.init
screen=pygame.display.set_mode((205,205))
screen.fill("white")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            image=pygame.image.load("light on.jpg")
            screen.blit(image,(0,0))
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            image=pygame.image.load("light off.jpg")
            screen.blit(image,(0,0))
            pygame.display.update()
        

            