import pygame
import sys
import random


pygame.init()


pygame.mixer.music.set_volume(.5)
musica_de_fundo = pygame.mixer.music.load("BoxCat Games - Victory.mp3")
pygame.mixer.music.play(-1)
som_ponto = pygame.mixer.Sound("coin.wav")
#som_ponto.set_volume(0)

comprimento = 50
largura = 640
altura = 480
posx = largura/2
posy = altura/2
#mover_esquerda = False
morreu = False
velocidade = 2
x_controle = velocidade
y_controle = 0
tela = pygame.display.set_mode((largura,altura))
titulo = pygame.display.set_caption("jogo")
relogio =pygame.time.Clock()
comprimento_inicial = comprimento


pontos = 0
fonte = pygame.font.SysFont("arial",40,bold=True,italic=True)
#print(pygame.font.get_fonts()) #ver todas as fontes disponiveis


posx_maca = random.randint(50,590)
posy_maca = random.randint(50,430)


lista_cobra = []
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))

def reiniciar_jogo():
    global pontos, comprimento_inicial,posx,posy, posx_maca, posy_maca,lista_cabeca,lista_cobra,morreu
    pontos = 0
    comprimento_inicial = comprimento
    posx = largura/2
    posy = altura/2
    posx_maca = random.randint(50,590)
    posy_maca = random.randint(50,430)
    lista_cabeca = []
    lista_cobra = []
    morreu = False

loop = True

while loop:
    relogio.tick(60)
    tela.fill((255,255,255))



    mensagem = f"Pontos:{pontos}"
    
    texto_formatado = fonte.render(mensagem,True,(0,0,0))
    mensagem2 =(f"você morreu, aperte R para recomeçar")
    texto_game_over = fonte.render(mensagem2,True, (0,0,0))    

    if posx > largura:
        posx = 0
    if posx < 0:
        posx = largura
    if posy > altura:
        posy = 0
    if posy < 0:
        posy = altura
    #if mover_esquerda == True:
    #    posx-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == pygame.K_d:
                if x_controle ==-velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == pygame.K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = - velocidade
            if event.key == pygame.K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

                
    posx += x_controle
    posy += y_controle
    """if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            mover_esquerda = False"""

    '''if pygame.key.get_pressed()[pygame.K_a]:
        posx -= 10
    if pygame.key.get_pressed()[pygame.K_d]:
        posx += 10
    if pygame.key.get_pressed()[pygame.K_w]:
        posy -= 10
    if pygame.key.get_pressed()[pygame.K_s]:
        posy += 10'''
    cobra = pygame.draw.rect(tela,(0,255,0),(posx,posy,20,20))
    maça = pygame.draw.rect(tela,(255,0,0), (posx_maca,posy_maca,20,20))

    if cobra.colliderect(maça):
        
        posx_maca = random.randint(50,590)
        posy_maca = random.randint(50,430)
        pontos+=1
        som_ponto.play()
        comprimento_inicial += 10
        



    lista_cabeca = []

    lista_cabeca.append(posx)
    lista_cabeca.append(posy)
    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) >1:
        morreu = True
        while morreu:
            
            tela.blit(texto_game_over,(20,200))
            tela.blit(texto_formatado,(450,40))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reiniciar_jogo()


    if len(lista_cobra) > comprimento_inicial:
        del (lista_cobra[0])
    aumenta_cobra(lista_cobra)
    



    tela.blit(texto_formatado,(450,40))


    #pygame.draw.circle(tela,(255,0,0),(20,50),60)
    #pygame.draw.line(tela,(0,0,255),(600,350),(0,200),5)
        
    pygame.display.update()