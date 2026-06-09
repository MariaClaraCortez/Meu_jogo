import pygame
from caminho_relativo import resource_path
from classe_garrafinhas import Garrafinhas

pygame.init()


clock = pygame.time.Clock()

#cria a janela do jogo
tela = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Beber ou Morrer")


lista_vidas = [Garrafinhas(resource_path('src/img/garrafa_azul.png')),
               Garrafinhas(resource_path('src/img/garrafa_rosa.png')),
               Garrafinhas(resource_path('src/img/garrafa_roxa.png')),
               Garrafinhas(resource_path('src/img/garrafa_verde.png')),
               Garrafinhas(resource_path('src/img/garrafa_vermelha.png'))]

status_jogo = "INICIO"

fundo = pygame.image.load(resource_path("src/img/fundo.png"))
fundo = pygame.transform.scale(fundo,(1200,800))
inicio = pygame.image.load(resource_path("src/img/inicio.png"))

rodando = True
while rodando:
    #pego todos os eventos que aconteceu na jaenla
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:   #percorro os eventos para encontrar aquele que eu quiser

        #se um dos eventos for igual a ... faça ...
        if evento.type == (pygame.QUIT): #ou 256
            rodando = False
        if evento.type == (pygame.K_ESCAPE): #ou 256
            rodando = False

    tecla_pressionada = pygame.key.get_pressed()

    if status_jogo == "INICIO":
        tela.blit(inicio,(0,0))
        if tecla_pressionada [pygame.K_RETURN] or tecla_pressionada [pygame.K_KP_ENTER]:
            status_jogo = "JOGANDO"
    if status_jogo == "JOGANDO":
         tela.blit(fundo,(0,0))









        
    pygame.display.update()
    
    clock.tick(100)








