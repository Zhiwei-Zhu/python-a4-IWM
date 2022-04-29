import math
from random import randrange
from numpy import place
import pygame

from player import Player

class Enemie:
    def __init__(self,ecran,x,y,dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.ecran = ecran
        self.vit = 0

    def Draw(self):
        pygame.draw.circle(self.ecran,(255,0,0),(self.x,self.y),10)
    
    def Update(self,deltatime):
        if self.dir == 0:
            self.x += -deltatime * self.vit
        if self.dir == 1:
            self.x += deltatime * self.vit
        self.y += deltatime * 200
    
    def Collision(self, player):
        if math.sqrt((player.x - self.x)**2+(player.y - self.y)**2) <= 20:
            player.playing = False
        if self.x < 0 or self.x > 1000 or player.playing == False:
            self.y = randrange(-600,0)
            self.x = randrange(0,1000)
            self.vit = 0