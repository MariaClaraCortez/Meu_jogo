import pygame
from caminho_relativo import resource_path
from classe_inimigo import Inimigo
from classe_jogador import Jogador
from classe_garrafinha import Vida



pygame.init()


clock = pygame.time.Clock()

#cria a janela do jogo
tela = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Beber ou Morrer")


lista_vidas = [Vida(resource_path('src/img/garrafa_azul.png')),
               Vida(resource_path('src/img/garrafa_rosa.png')),
               Vida(resource_path('src/img/garrafa_roxa.png')),
               Vida(resource_path('src/img/garrafa_verde.png')),
               Vida(resource_path('src/img/garrafa_vermelha.png'))]

status_jogo = "INICIO"

fundo = pygame.image.load(resource_path("src/img/fundo.png"))
fundo = pygame.transform.scale(fundo,(1200,800))
inicio = pygame.image.load(resource_path("src/img/inicio.png"))



pontos = 0
vidas = 3
coelho = Jogador()
fonte_texto = pygame.font.SysFont("Arial",20,True)
fonte_text = pygame.font.SysFont("Segoe UI Emoji",18,True)


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
        texto_vidas =fonte_text.render(f"VIDAS: {'❤'*vidas}",False,(0,0,0))
        tela.blit(texto_vidas,(500,65))
        texto_pontos =fonte_texto.render(f"PONTOS: {pontos}",False,(0,0,0))
        tela.blit(texto_pontos,(520,40))


        coelho.andar(tecla_pressionada)
        coelho.exbir(tela)

        for vida in lista_vidas:
            vida.andar()
            vida.exibir(tela)

            if coelho.contorno.overlap(vida.contorno,(vida.pos_imagem_x - coelho.pos_imagem_x,vida.pos_imagem_y - coelho.pos_imagem_y)):
                mortes += 1
                vida.voltar()
        for inimigo in lista_inimigos:
            inimigo.andar()
            inimigo.exibir(tela)

            if coelho.contorno.overlap(inimigo.contorno,(inimigo.pos_imagem_x - coelho.pos_imagem_x,inimigo.pos_maca_y - coelho.pos_imagem_y)):
                mortes -= 1
                coelho.morte()
                coelho.voltar()
                if mortes == 0:
                    status_jogo = "PERDEU"


  
    pygame.display.update()
    
    clock.tick(100)








