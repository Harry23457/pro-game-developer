import pygame
pygame.init()
screen=pygame.display.set_mode((700,700))
winner=""
gameover=False
pygame.display.set_caption("space invaders")
image1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("space r.png"),(50,50)),90)
image2=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("space y.png"),(50,50)),270)
bg=pygame.transform.scale(pygame.image.load("space ship land.png"),(700,700))
border=pygame.Rect(345,0,30,700)
rhealth=10
yhealth=10
yellow=pygame.Rect(100,350,50,50)
red=pygame.Rect(600,350,50,50)
redbullet=[]
yellowbullet=[]
def draw():
    screen.blit(bg,(0,0))
    screen.blit(image1,(yellow.x,yellow.y))
    screen.blit(image2,(red.x,red.y))
    pygame.draw.rect(screen,"black",border)
    font=pygame.font.SysFont("times new roman",40)
    text1=font.render("Health:"+str(rhealth),True,"white")
    screen.blit(text1,(500,50))
    text2=font.render("Health:"+str(yhealth),True,"white")
    screen.blit(text2,(50,50))
    for i in redbullet:
        pygame.draw.rect(screen,"red",i)
    for i in yellowbullet:
        pygame.draw.rect(screen,"yellow",i)
    text3=font.render("Game over winner is "+winner,True,"white")
    if gameover==True:
        screen.blit(text3,(170,350))


    
def yellow_move(keys):
    if keys[pygame.K_a] and yellow.x>0:
        yellow.x-=5
    if keys[pygame.K_d] and yellow.x<290:
        yellow.x+=5
    if keys[pygame.K_w] and yellow.y>0:
        yellow.y-=5
    if keys[pygame.K_s] and yellow.y<650:
        yellow.y+=5

def red_move(keys):
    if keys[pygame.K_RIGHT] and red.x<650:
        red.x+=5
    if keys[pygame.K_LEFT] and red.x>380:
        red.x-=5
    if keys[pygame.K_UP] and red.y>0:
        red.y-=5
    if keys[pygame.K_DOWN] and red.y<650:
        red.y+=5

def hit(yellowbullet,redbullet):
    global rhealth,yhealth
    if gameover==False:
       
        for i in yellowbullet:
            i.x+=10
            if red.colliderect(i):
                rhealth-=1
                yellowbullet.remove(i)
            elif i.x==700:
                yellowbullet.remove(i)
        for i in redbullet:
            i.x-=10
            if yellow.colliderect(i):
                yhealth-=1
                redbullet.remove(i)
            elif i.x==0:
                if yellow.colliderect(i):
                  yhealth-=1
                  redbullet.remove(i)


def go():
    global winner,gameover
    if yhealth==0:
        winner="red"
        gameover=True
    if rhealth==0:
        winner="yellow"
        gameover=True









  
          

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_f:
                bullet=pygame.Rect(yellow.x+25,yellow.y+25,8,4)
                yellowbullet.append(bullet)
            if event.key==pygame.K_RSHIFT:
                bullet=pygame.Rect(red.x,red.y+25,8,4)
                redbullet.append(bullet)

    draw()
    keys=pygame.key.get_pressed()
    yellow_move(keys)
    red_move(keys)
    hit(yellowbullet,redbullet)
    go()
    pygame.display.update()



