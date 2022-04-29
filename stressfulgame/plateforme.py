import pygame

from enemie import Enemie
from player import Player

class Plateform:
    def __init__(self,ecran, width, height , x , y ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ecran = ecran

    def Draw(self):
       pygame.draw.rect(self.ecran,(211,236,49), pygame.Rect(self.x , self.y , self.width , self.height))
    
    def Collision(self, player):
        if self.y  <= player.y + 10 and player.x+10 >= self.x:
                if player.x - 10 <= self.x + self.width and player.y-10 <= self.y+self.height:
                    x = self.x + self.width/2
                    y = self.y + self.height/2
                    if player.y > self.y and player.y < self.y+self.height:
                        if player.x < x:
                            if type(player) == Enemie:
                                player.dir = 0
                            player.x = self.x-10
                        if player.x > x:
                            if type(player) == Enemie:
                                player.dir = 1
                            player.x = self.x+self.width+10
                    if player.x > self.x and player.x< self.x + self.width:
                        if player.y < y:
                            player.y = self.y-10
                            if type(player) == Player:
                                if player.y <= 100:
                                    player.win = True      
                                player.canjump = True
                                player.vit = 500
                            if type(player) == Enemie:
                                player.vit = 100
                        if player.y > y:
                            if type(player) == Player:
                                player.jump = 0
                            player.y = self.y+self.height+10
                    
