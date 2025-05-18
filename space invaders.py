import pygame
pygame.init()
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("space invaders")
image1=pygame.image.load("space r.png")
image2=pygame.image.load("space y.png")
bg=pygame.image.load("space ship landing.py")
def draw():
    screen.blit(bg,(0,0))
    screen.blit(image1,(100,350))
    screen.blit(image2,(600,350))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    draw()