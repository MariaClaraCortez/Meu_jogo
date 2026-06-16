import pygame
import random

class Bonus:
    
    def __init__(self,endereco_imagem):
        self.imagem = pygame.image.load(endereco_imagem)
        self.imagem = pygame.transform.scale(self.imagem,(60,60))

        self.pos_imagem_y = 0
        self. lugares = [300,400,500,600,700,800,900,1000]
        self.pos_imagem_x = random.choice(self.lugares)
        self.velocidade = random.randint(5,8)

        self.mascara = pygame.mask.from_surface(self.imagem)

    def exibir(self, tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_imagem_x,self.pos_imagem_y))