import pygame
pygame.init()
screen=pygame.display.set_mode([1000,700])
pygame.display.set_caption("Bouncing Ball")
screen.fill("black")
rc=pygame.draw.circle(surface=screen,color="red",center=[100,100],radius=50)
speed =[1,1]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("black")
    rc=rc.move (speed)
    #code for ball change in direction
    if rc.left<=0 or rc.right>=1000:
        speed[0]=-speed[0]
    if rc.top<=0 or rc.bottom>=700:
        speed[1]=-speed[1]   
    
    pygame.draw.circle(surface=screen,color="red",center=rc.center,radius=50)
    pygame.display.update()