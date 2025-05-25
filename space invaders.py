import pygame
pygame.init()
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("space invaders")
image1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("space r.png"),(50,50)),90)
image2=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("space y.png"),(50,50)),270)
bg=pygame.transform.scale(pygame.image.load("space ship land.png"),(700,700))
border=pygame.Rect(345,0,30,700)
rhealth=10
yhealth=10
def draw():
    screen.blit(bg,(0,0))
    screen.blit(image1,(100,350))
    screen.blit(image2,(600,350))
    pygame.draw.rect(screen,"black",border)
    font=pygame.font.SysFont("times new roman",40)
    text1=font.render("Health:"+str(rhealth),True,"white")
    screen.blit(text1,(500,50))
    text2=font.render("Health:"+str(yhealth),True,"white")
    screen.blit(text2,(50,50))

    

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    draw()
    pygame.display.update()


