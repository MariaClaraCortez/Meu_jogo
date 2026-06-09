import pygame
from caminho_relativo import resource_path



class Jogador:

    def __init__(self):

        lista_coelhos= [pygame.image.load(resource_path('src/img/indo_direita.png')),
                        pygame.image.load(resource_path('src/img/indo_esquerda.png'))]
        self.imagem = lista_coelhos[0]

        self.imagem = pygame.transform.scale(self.imagem,(100,100))
        self.imagem = pygame.mask.from_surface(self.imagem)

        self.pos_imagem_x = 100
        self.pos_imagem_y = 100
        

    def andar(self,tecla_pressionada):
        if tecla_pressionada [pygame.K_RIGHT]:  
            if self.pos_imagem_x < 1200 - self.imagem.get_width():
             self.pos_imagem_x +=10
        if tecla_pressionada [pygame.K_LEFT]:
            if self.pos_imagem_x > 0:
                self.pos_imagem_x = self.pos_imagem_x - 10
    
    def exbir(self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_imagem_x,self.pos_imagem_y))

    def voltar (self):
        self.pos_imagem_x = 100
        self.pos_imagem_y = 100

    