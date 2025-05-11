import pygame
import random

pygame.init()
colors=["black","red","green","yellow","blue","orange","purple","teal"]
currentc="black"
screen=pygame.display.set_mode((700,700))
sw1=False
position=None
screen.fill("white")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                sw1=True
                position=event.pos
                pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                sw1=False
                pygame.display.update()
        elif event.type==pygame.MOUSEMOTION:
            if sw1:
                currentpos=event.pos
                pygame.draw.line(screen,currentc,position,currentpos)
                position=currentpos
                pygame.display.update()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                #cr=random.choice(colors)
                #pygame.draw.line(screen,cr,position,currentpos)
                cindex=colors.index(currentc)
                cindex+=1
                if cindex>=7:
                    cindex=0
                currentc=colors[cindex]
                pygame.display.update()



    