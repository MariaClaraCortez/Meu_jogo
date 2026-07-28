import pygame
import random
from caminho_relativo import resource_path  # posso colocar  (as pr) para abreviar
from classe_inimigo import Inimigo
from classe_jogador import Jogador
from classe_garrafinha import Vida



pygame.init()


clock = pygame.time.Clock()

#cria a janela do jogo
tela = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Corida de Campeões")



lista_vidas = [Vida(resource_path('src/img/garrafa_azul.png')),
               Vida(resource_path('src/img/garrafa_rosa.png')),
               Vida(resource_path('src/img/garrafa_roxa.png')),
               Vida(resource_path('src/img/garrafa_verde.png')),
               Vida(resource_path('src/img/garrafa_vermelha.png'))]

lista_inimigos = [Inimigo(resource_path('src/img/refri.png')),
                  Inimigo(resource_path('src/img/hamburguer.png')),
                  Inimigo(resource_path('src/img/batata.png'))]

status_jogo = "INICIO"

fundo = pygame.image.load(resource_path("src/img/fundo2.png"))
fundo = pygame.transform.scale(fundo,(1200,800))
inicio = pygame.image.load(resource_path("src/img/inicio2.png"))
inicio = pygame.transform.scale(inicio,(1200,800))
perdeu = pygame.image.load(resource_path("src/img/perdeu.png"))
ganhou = pygame.image.load(resource_path("src/img/ganhou.png"))
pause = pygame.image.load(resource_path("src/img/pause.png"))

lista_bonus = [Vida(resource_path('src/img/barrinha.png'))]

som_vitoria = pygame.mixer.Sound(resource_path("sons/ganhou.mp3"))
som_poder = pygame.mixer.Sound(resource_path("sons/poder.mp3"))
som_inicio = pygame.mixer.Sound(resource_path("sons/inicio.mp3"))
som_jogo = pygame.mixer.Sound(resource_path("sons/jogo.mp3"))

segundos = 5
conta = 0
poder = False
uso = 3
pontos = 0
vidas = 3
coelho = Jogador()
cont_sprite = 0
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
        som_inicio.play()
        tela.blit(inicio,(0,0))
        if tecla_pressionada [pygame.K_RETURN] or tecla_pressionada [pygame.K_KP_ENTER]:
            status_jogo = "JOGANDO"
            som_inicio.stop()
    if status_jogo == "JOGANDO":
        som_jogo.play()
        tela.blit(fundo,(0,0))
        texto_vidas =fonte_text.render(f"VIDAS: {'❤'*vidas}",False,(0,0,0))
        tela.blit(texto_vidas,(500,65))
        texto_pontos =fonte_texto.render(f"PONTOS: {pontos}",False,(0,0,0))
        tela.blit(texto_pontos,(520,40))
        texto_poderes = fonte_texto.render(f"PODERES: {uso}",False,(0,0,0))
        tela.blit(texto_poderes,(100,755))
        

        cont_sprite += 1
        if cont_sprite > 10:
            cont_sprite = 0
        coelho.andar(tecla_pressionada,cont_sprite)
        coelho.exbir(tela)

        for bonus in lista_bonus:
            if poder == False:
                bonus.velocidade = random.randint(3,8)
                bonus.andar()
                bonus.exibir(tela)
                if coelho.mascara.overlap(bonus.mascara,(bonus.pos_imagem_x - coelho.pos_imagem_x,bonus.pos_imagem_y - coelho.pos_imagem_y)):
                    som_jogo.stop()
                    bonus.colidir()
                    vidas += 1
                    bonus.voltar()



        for vida in lista_vidas:
            if poder == True:
                vida.velocidade = random.randint(9,15)
            vida.andar()
            vida.exibir(tela)

            if coelho.mascara.overlap(vida.mascara,(vida.pos_imagem_x - coelho.pos_imagem_x,vida.pos_imagem_y - coelho.pos_imagem_y)):
                vida.beber()
                pontos += 1
                vida.voltar()
        for inimigo in lista_inimigos:
            if poder == False:
                inimigo.andar()
                inimigo.exibir(tela)
            else:
                inimigo.voltar()


            if coelho.mascara.overlap(inimigo.mascara,(inimigo.pos_imagem_x - coelho.pos_imagem_x,inimigo.pos_imagem_y - coelho.pos_imagem_y)):
                inimigo.mordida()
                vidas -= 1
                inimigo.voltar()
                inimigo.exibir(tela)
                coelho.voltar()
                if vidas == 0:
                    coelho.morte()
                    som_jogo.stop()
                    status_jogo = "PERDEU"


    
        if tecla_pressionada [pygame.K_SPACE] and uso >=1 and poder == False:
            som_poder.play()
            poder = True
            uso -=1
        
        if poder == True:
            conta += 1 
            texto_segundos = fonte_texto.render(f"SEGUNDOS: {segundos}",False,(0,0,0))
            tela.blit(texto_segundos,(220,755))
            if conta >= 60:
                segundos -= 1
                conta = 0
            if segundos <= 0:
                segundos = 5
                poder = False
    if tecla_pressionada[pygame.K_q]:
        status_jogo = "PAUSE"

    if status_jogo == "PAUSE":
        tela.blit(pause,(0,0))
        if tecla_pressionada [pygame.K_RETURN]or tecla_pressionada [pygame.K_KP_ENTER]:
            status_jogo = "JOGANDO"
        if tecla_pressionada [pygame.K_ESCAPE]: 
            rodando = False

    if status_jogo == "PERDEU":
        tela.blit(perdeu,(0,0))
        if tecla_pressionada [pygame.K_RETURN]or tecla_pressionada [pygame.K_KP_ENTER]:
            status_jogo = "INICIO"
            vidas = 3
            pontos = 0 
            uso = 3
            
    if pontos == 20:
            som_jogo.stop()
            som_vitoria.play()
            status_jogo = "VITORIA"

    if status_jogo == "VITORIA":
        tela.blit(ganhou,(0,0))
        if tecla_pressionada [pygame.K_RETURN]or tecla_pressionada [pygame.K_KP_ENTER]:
            status_jogo = "INICIO"
            vidas = 3
            pontos = 0 
            uso = 3                  

            



  
    pygame.display.update()
    
    clock.tick(60)








