import pygame
import random

class Vida:
    
    def __init__(self,endereco_imagem):
        self.imagem = pygame.image.load(endereco_imagem)
        self.imagem = pygame.transform.scale(self.imagem,(60,60))

        self.pos_maca_y = 0
        self. lugares = [300,400,500,600,700,800,900,1000]
        self.pos_maca_x = random.choice(self.lugares)
        self.velocidade = random.randint(5,8)

        self.contorno = pygame.mask.from_surface(self.imagem)


    def andar(self):
        self.pos_maca_y = self.pos_maca_y + self.velocidade
        if self.pos_maca_y>= 1000:
            self.voltar()

   


    def exibir(self, tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_maca_x,self.pos_maca_y))

    def voltar (self):
        self.pos_maca_y = 0
        self.pos_maca_x = random.choice(self.lugares)
        self.velocidade = random.randint(5,14)