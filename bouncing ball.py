import pygame
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Bouncing Ball")
screen.fill("black")
rc=pygame.draw.circle(surface=screen,color="red",center=[100,100],radius=50)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("black")
    rc=rc.move([1,1])
    pygame.draw.circle(surface=screen,color="red",center=rc.center,radius=50)
    pygame.display.update()