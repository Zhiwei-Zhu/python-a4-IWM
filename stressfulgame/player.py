import pygame

class Player:
    def __init__(self, ecran):
        self.x = 50
        self.y = 500
        self.vit = 0
        self.canjump = False
        self.jump = 0
        self.maxjump = 600
        self.ecran = ecran
        self.playing = True
        self.win = False

    def Draw(self):
        pygame.draw.circle(self.ecran, (0, 0, 255), (self.x, self.y), 10)

    def Update(self, deltatime):
        #mouvement
        if pygame.key.get_pressed()[pygame.K_q]:
            self.x += -deltatime * self.vit
        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += deltatime * self.vit
        
        #gravité    
        self.y += deltatime * 300
        self.Jumping(deltatime)
    
    def Jumping(self,deltatime):
        self.y -= deltatime * self.jump
        if self.jump > 0:
            self.jump -= deltatime * 300

    #reset
    def Reset(self):
        if self.y >= 1300:
            print(self.y)
            self.y = 500
            self.x = 50
            print("reset")

    #in case you lose
    def losing(self):
        font = pygame.font.Font(None, 50)
        text = font.render("You Lose",True,(255,255,255))
        text2 = font.render("To Retry press Space",True,(255,255,255))
        textRect = text.get_rect()
        textRect.center = ( 500, 500)
        textRect2 = text2.get_rect()
        textRect2.center = ( 500, 600)

        self.ecran.fill((242,119,17))
        self.ecran.blit(text, textRect)
        self.ecran.blit(text2,textRect2)
        self.y = 500
        self.x = 50
        self.vit =0
        self.canjump = False
        
    #in case you win
    def winning(self):
        font = pygame.font.Font(None, 50)
        text = font.render("You Won",True,(255,255,255))
        text2 = font.render("To play again press Space",True,(255,255,255))
        textRect = text.get_rect()
        textRect.center = ( 500, 500)
        textRect2 = text2.get_rect()
        textRect2.center = ( 500, 600)

        self.ecran.fill((242,119,17))
        self.ecran.blit(text, textRect)
        self.ecran.blit(text2,textRect2)
        self.y = 500
        self.x = 50
        self.vit =0
        self.canjump = False