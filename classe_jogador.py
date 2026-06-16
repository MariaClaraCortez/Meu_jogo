import pygame
from caminho_relativo import resource_path



class Jogador:

    def __init__(self):

        self.lista_coelhos=[pygame.transform.scale(pygame.image.load(resource_path('src/img/indo_direita.png')),(130,180)),
                            pygame.transform.scale(pygame.image.load(resource_path('src/img/indo_esquerda.png')),(130,180))]
        self.contador_de_sprite = 0
        self.sprite = self.lista_coelhos[self.contador_de_sprite]
        self.imagem = self.sprite
        self.mascara = pygame.mask.from_surface(self.imagem)
        self.som_morte = pygame.mixer.Sound(resource_path("sons/perdeu.mp3"))
        self.som_vitoria = pygame.mixer.Sound(resource_path("sons/ganhou.mp3"))
        self.som_poder = pygame.mixer.Sound(resource_path("sons/poder.mp3"))
        self.som_inicio = pygame.mixer.Sound(resource_path("sons/inicio.mp3"))
        self.som_jogo = pygame.mixer.Sound(resource_path("sons/jogo.mp3"))

        self.pos_imagem_x = 100
        self.pos_imagem_y = 520
        

    def andar(self,tecla_pressionada):
        if tecla_pressionada[pygame.K_RIGHT] or tecla_pressionada [pygame.K_LEFT]:
            self.contador_de_sprite += 1
            if self.contador_de_sprite > 1:
                self.contador_de_sprite = 0
            self.imagem = self.lista_coelhos[self.contador_de_sprite]
        if tecla_pressionada [pygame.K_RIGHT]:  
            if self.pos_imagem_x < 1200 - self.imagem.get_width():
             self.pos_imagem_x +=10
        if tecla_pressionada [pygame.K_LEFT]:
            if self.pos_imagem_x > 0:
                self.pos_imagem_x = self.pos_imagem_x - 10
                self.imagem = pygame.transform.flip(self.imagem,True,False)
    
    def exbir(self,tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_imagem_x,self.pos_imagem_y))

    def voltar (self):
        self.pos_imagem_x = 100
        self.pos_imagem_y = 520

    def morte (self):
        self.som_morte.play()

    def vitoria (self):
        self.som_vitoria.play()
    
    def poder (self):
        self.som_poder.play()

    def inicio (self):
        self.som_inicio.play()
    
    def jogo (self):
        self.som_jogo.play()