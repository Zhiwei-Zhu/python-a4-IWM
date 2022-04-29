from random import randrange
from tkinter import E
import pygame
from enemie import Enemie
from player import Player
from plateforme import Plateform
pygame.init()

ecran = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("jeu")
plateformList= []
enemieList = []
perso = Player(ecran)
sol = Plateform(ecran, 1200, 200,-100 ,800)
i = 0
loop = True
getTickLastFrame = 0
while loop:
    if perso.win:
        perso.winning()
        i = 0
        enemieList.clear()
        plateformList.clear()
    if perso.playing == False:
        perso.losing()
        enemieList.clear()
    if perso.playing and perso.win == False :
        if len(plateformList)< 10:
            i += 1
            y = i*100
            x = randrange(80,980)
            plateformList.append(Plateform(ecran, 20, 10, x , y))
        if len(enemieList)< 20:
            enemieList.append(Enemie(ecran, randrange(0, 1000), randrange(-1000,0), randrange(0,1)))
        time = pygame.time.get_ticks()
        deltaTime = (time - getTickLastFrame)/1000.0
        getTickLastFrame = time
        perso.Update(deltaTime)
        perso.Reset()
        for plat in plateformList:
            plat.Collision(perso)
            for en in enemieList:
                plat.Collision(en)
                sol.Collision(en)
        for en in enemieList:
            en.Update(deltaTime)
            en.Collision(perso)

        sol.Collision(perso)
        ecran.fill((0,0,0))
        sol.Draw()
        for plat in plateformList:
            plat.Draw()

        perso.Draw()
        for en in enemieList:
            en.Draw()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if type(perso)== Player:
                        if perso.canjump:
                            perso.canjump = False
                            perso.jump = perso.maxjump
            if event.type == pygame.QUIT:
                loop = False
         
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    if perso.playing == False:
                        perso.playing = True
                    if perso.win == True:
                        perso.win = False
        if event.type == pygame.QUIT:
            loop = False
         
    
    pygame.display.flip()



pygame.quit()