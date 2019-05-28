 #-*- coding: utf-8 -*-
import pygame
import time
import os
import sys
from pygame import mouse

white = (255,255,255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 180, 0)
blue = (0, 0, 170)
greem = (0, 255, 0)
redi = (255, 0 , 0)
blu = (0, 0, 130)

pygame.init()
tela = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Mustache's Anatomy")
relogio = pygame.time.Clock()

pygame.mixer.music.load("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/sons/som.mp3")
pygame.mixer.music.play(-1) 

ta = [
        ["C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase1/garota1.png", "CABEÇA", "BRAÇO", "TRONCO", "PERNA", "Qual parte do corpo da menina","a seta está apontando?"]
        ,["C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase1/garota2.png"] 
        ,["C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase1/garota3.png"]
        ,["C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase1/garota4.png"]
    ]

ta1 = [
        ["C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase2/Coração.jpeg", "Coração", "Fígado", "Pulmão","Intestino","Qual nome do orgão", "a seta está apontando?"]
        ,["C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase2/Fígado.jpeg"]
        ,["C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase2/Pulmão.jpeg"]
        ,["C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase2/intestino.jpeg"]
]



def texto(text1, x, y):
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render(text1, True, black)
    textRect = text.get_rect() 
    textRect.center = (x, y // 2)
    tela.blit(text, textRect)

def texto2(text1, x, y):
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render(text1, True, white)
    textRect = text.get_rect() 
    textRect.center = (x, y // 2)
    tela.blit(text, textRect)


def img(local, x, y):
    img= pygame.image.load (os.path.join (local))
    tela.blit (img, (x, y))

def botao(msg, x, y, w, h, ca, ci, acao = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print (click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(tela, ci,(x, y, w, h))
        if click[0] == 1 and acao != None:
            if acao == "jogar":
                fase1()
            elif acao == "pergunta2":
                pergunta2()
            elif acao == "pergunta3":
                pergunta3()
            elif acao == "pergunta4":
                pergunta4()
            elif acao == "fase2":
                fase2()
            elif acao == "pergunta21":
                pergunta21()
            elif acao == "pergunta31":
                pergunta31()
            elif acao == "pergunta41":
                pergunta41()
            elif acao == "fase3":
                fase3()
            elif acao == "fase4":
                fase4()
            elif acao == "menu":
                menu()
            elif acao == "gameLoop":
                gameLoop()
            elif acao == "sair":
                pygame.quit()
            
            
                
    else:       
        pygame.draw.rect(tela, ca,(x, y, w, h))
    font = pygame.font.Font('freesansbold.ttf', 24) 
    text = font.render(msg, True, black)
    textRect = text.get_rect() 
    textRect.center = ((x+(w/2)), (y+(h/2)) )
    tela.blit(text, textRect)



def fase1():

    sair = True 
    tela.fill(white)
    img(ta[0][0], 20, 100)
    texto(ta[0][5], 800, 350)
    texto(ta[0][6], 800, 450)
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
  
        botao(ta[0][1], 700, 300, 200, 30, ci = green, ca = white, acao =  "pergunta2")
        botao("ÓCULOS", 700, 350, 200, 30, ci = green, ca = white, acao =  None)
        botao("BOCA", 700, 400, 200, 30, ci = green, ca = white, acao = None)
        botao("SETA", 700, 450, 200, 30, ci = green, ca = white, acao = None)
        
        pygame.display.update()
        relogio.tick(30)
        
    


def pergunta2():

    sair = True
    tela.fill(white)
    img(ta[3][0], 20, 100)  
    texto(ta[0][5], 800, 350)
    texto(ta[0][6], 800, 450)
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
            
        botao("BOTA", 700, 300, 200, 35, ci = green, ca = white, acao = None)
        botao(ta[0][4], 700, 350, 200, 35, ci = green, ca = white, acao = "pergunta3")
        botao("PÉ", 700, 400, 200, 35, ci = green, ca = white, acao = None)
        botao("COXA", 700, 450, 200, 35, ci = green, ca = white, acao = None)

        pygame.display.update()
        relogio.tick(30)


def pergunta3():

    sair = True 
    tela.fill(white)
    img(ta[2][0], 20, 100)
    texto(ta[0][5], 800, 350)
    texto(ta[0][6], 800, 450)
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
          
        botao("UMBIGO", 700, 300, 200, 35, ci = green, ca = white, acao = None)
        botao("BRAÇO", 700, 350, 200, 35, ci = green, ca = white, acao = None)
        botao("CAMISA", 700, 400, 200, 35, ci = green, ca = white, acao = None)
        botao(ta[0][3], 700, 450, 200, 35, ci = green, ca = white, acao = "pergunta4")
        

        pygame.display.update()
        relogio.tick(30)
   


def pergunta4():

    sair = True 
    tela.fill(white)
    img(ta[1][0], 20, 100)
    texto(ta[0][5], 800, 350)
    texto(ta[0][6], 800, 450)
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
        
        botao("MÃO", 700, 300, 200, 35, ci = green, ca = white, acao = None)
        botao("PULSO", 700, 350, 200, 35, ci = green, ca = white, acao = None)
        botao(ta[0][2], 700, 400, 200, 35, ci = green, ca = white, acao = "fase2")
        botao("CACHORRO", 700, 450, 200, 35, ci = green, ca = white, acao = None)
        

        pygame.display.update()
        relogio.tick(30)


def fase2():
    sair = True
    tela.fill( white )
    img( ta1[0][0], 0, 0 )
    texto(ta1[0][5], 800, 350)
    texto(ta1[0][6], 800, 450)
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        botao( ta1[0][1], 700, 300, 200, 35, ci=green, ca=white, acao="pergunta21" )
        botao( ta1[0][2], 700, 350, 200, 35, ci=green, ca=white, acao= None )
        botao( ta1[0][3], 700, 400, 200, 35, ci=green, ca=white, acao= None )
        botao( ta1[0][4], 700, 450, 200, 35, ci=green, ca=white, acao= None )

        pygame.display.update()
        relogio.tick( 30 )

def pergunta21():
    sair = True
    tela.fill( white )
    img( ta1[3][0], 0, 0 )
    texto(ta1[0][5], 800, 350)
    texto(ta1[0][6], 800, 450)
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        botao( ta1[0][2], 700, 300, 200, 35, ci=green, ca=white, acao=None  )
        botao( ta1[0][3], 700, 350, 200, 35, ci=green, ca=white, acao=None  )
        botao( ta1[0][4], 700, 400, 200, 35, ci=green, ca=white, acao="pergunta31" )
        botao( ta1[0][1], 700, 450, 200, 35, ci=green, ca=white, acao=None  )

        pygame.display.update()
        relogio.tick( 30 )


def pergunta31():
    sair = True
    tela.fill( white )
    img( ta1[2][0], 0, 0 )
    texto(ta1[0][5], 800, 350)
    texto(ta1[0][6], 800, 450)
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        botao( ta1[0][2], 700, 300, 200, 35, ci=green, ca=white, acao=None  )
        botao( ta1[0][1], 700, 350, 200, 35, ci=green, ca=white, acao=None  )
        botao( ta1[0][4], 700, 400, 200, 35, ci=green, ca=white, acao=None  )
        botao( ta1[0][3], 700, 450, 200, 35, ci=green, ca=white, acao="pergunta41" )

        pygame.display.update()
        relogio.tick( 30 )

def pergunta41():
    sair = True
    tela.fill( white )
    img( ta1[1][0], 0, 0 )
    texto(ta1[0][5], 800, 350)
    texto(ta1[0][6], 800, 450)
    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        botao( ta1[0][4], 700, 300, 200, 35, ci=green, ca=white, acao=None )
        botao( ta1[0][3], 700, 350, 200, 35, ci=green, ca=white, acao=None  )
        botao( ta1[0][2], 700, 400, 200, 35, ci=green, ca=white, acao="fase3")
        botao( ta1[0][1], 700, 450, 200, 35, ci=green, ca=white, acao=None )

        pygame.display.update()
        relogio.tick( 30 )


def menu():

    sair = True 

    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        tela.fill(white)
    

        font = pygame.font.Font('freesansbold.ttf', 80) 
        text = font.render("Anatomia Humana", True, black)
        textRect = text.get_rect() 
        textRect.center = ((1080/2), (720 // 2))
        tela.blit(text, textRect)

        img('D:ESTUDO/hospital.jpg',0, 0)

        botao("JOGAR", 360, 650, 100, 50, ci = greem, ca = green, acao = "jogar")
        botao("SAIR", 540, 650, 100, 50, ci = redi, ca = red, acao = "sair")
        botao("TUTORIAL", 700, 650, 125, 50, ci = blue , ca = blu, acao = "tutorial")


        pygame.display.update()
        relogio.tick(30)




# Cria uma classe para armazenar os atributos do nosso heroi
class Hero(object):
    # Deixei alguns valores por padrao apenas por comodidade
    def __init__(self, image_path = "D:/ESTUDO/", scale = (100,160), position = [100, 200]):
        # Caminho para a imagem que ira representar o heroi
        self.image_path = image_path
            # Posicao inicial do heroi na tela
        self.position = position
        # Escala fixa do heroi
        self.scale = scale
        # Variavel utilizada para saber se o heroi esta selecionado ou nao
        self.held = False

        # Carrega a imagem do heroi
        self.image = pygame.image.load(self.image_path).convert_alpha()
        # Redimensiona a imagem para a escala definida
        self.image = pygame.transform.scale(self.image, self.scale)
def fase3():
    # Classe principal responsavel pela logica do jogo
    class Game(object):
        def __init__(self):
            # Inicializa a biblioteca pygame
            pygame.init()

            # Define a largura e altura da janela em pixels 600x400
            self.main_window = pygame.display.set_mode((1080, 720))

            # Define um nome para a janela
            pygame.display.set_caption("Drag and Drop")

            # Utiliza uma lista para armazenar os herois do jogo
            self.heroes = []

            # Utilizado para controlar a velocidade de quadros (de atualizacoes da tela)
            self.clock = pygame.time.Clock()

        # Funcao utilizada para criar e carregar a imagem de todos os herois
        def create_heroes(self):
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase3/intestino.png", (100, 100), [50, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase3/pulmao.png", (140, 140), [200, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase3/figado.png", (90, 50), [400, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase3/coracao.png", (70, 70), [600, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase3/rim.png", (75, 60), [800, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase3/cerebro.png", (75, 75), [1000, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase3/bigode.png", (150, 100), [500, 150]))

        # Funcao utilizada para verificar se a posicao do mouse esta em cima
        # de um heroi (passado por parametro)
        def is_over(self, mouse_pos, hero):
            # Verifica a posicao no eixo X
            if mouse_pos[0] > hero.position[0] and mouse_pos[0] < hero.position[0] + hero.scale[0]:
                # Verifica a posicao no eixo Y
                if mouse_pos[1] > hero.position[1] and mouse_pos[1] < hero.position[1] + hero.scale[1]:
                    return True
            return False

        # Funcao chamada quando o usuario clica com o mouse
        def mouse_button_down(self):
            # Obtem a posicao atual do mouse
            mouse_pos = mouse.get_pos()

            for i in range(0, len(self.heroes)):
                # Somente "ativa" a imagem_selecionada se o usuario clicou em cima da imagem
                if self.is_over(mouse_pos, self.heroes[i]):
                    self.heroes[i].held = True

        # Funcao chamada quando o usuario solta o botao do mouse
        def mouse_button_up(self):
            # 'Libera' todos os herois
            for i in range(0, len(self.heroes)):
                self.heroes[i].held = False

        # Funcao responsavel por atualizar a posicao de todos os herois
        def update_position(self):
            # Obtem a posicao atual do mouse
            mouse_pos = mouse.get_pos()

            for i in range(0, len(self.heroes)):
                # Se a variavel imagem_selecionada estiver "ativa" (True), atualiza a posicao da imagem
                if self.heroes[i].held:
                    # Define as posicoes X e Y da imagem, posiciona a imagem com o mouse centralizado
                    self.heroes[i].position[0] = mouse_pos[0] - self.heroes[i].scale[0]/2
                    self.heroes[i].position[1] = mouse_pos[1] - self.heroes[i].scale[1]/2

        # Funcao que roda o jogo
        def run(self):
            # Chama a funcao para criar os herois
            self.create_heroes()

            # Loop principal do jogo
            while True:

                # Verifica se algum evento aconteceu
                for event in pygame.event.get():
                    # Verifica se foi um evento de saida (pygame.QUIT), em caso afirmativo fecha a aplicacao
                    if event.type == pygame.QUIT: 
                        sys.exit()
                    # Se o usuario soltar o botao do mouse "ativa" a variavel imagem_selecionada
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_button_down()
                    # Se o usuario soltar o botao do mouse "desativa" a variavel imagem_selecionada
                    elif event.type == pygame.MOUSEBUTTONUP:
                        self.mouse_button_up()

                # Chama a funcao que atualiza a posicao dos herois
                self.update_position()
                self.main_window.fill(white)
                # Preenche a tela com uma cor, neste caso preto (definido logo apos importar as bibliotecas)
                img = pygame.image.load (os.path.join ("D:/ESTUDO/fase3/corponu.png"))
                self.main_window.blit(img, ((1080/3), (720/3)))
                
                botao("Confirmar", 900, 650, 120, 50, ci = greem, ca = green, acao = "fase4")

                # Coloca a imagem de todos os herois na tela com base na posicao
                for i in range(0, len(self.heroes)):
                    self.main_window.blit(self.heroes[i].image, self.heroes[i].position)
                
                # Atualiza a tela visivel ao usuario
                pygame.display.flip()

                # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
                self.clock.tick(60)

    if __name__ == "__main__":
        game = Game()
        game.run()


def fase4():
    # Classe principal responsavel pela logica do jogo
    class Game(object):
        def __init__(self):
            # Inicializa a biblioteca pygame
            pygame.init()

            # Define a largura e altura da janela em pixels 600x400
            self.main_window = pygame.display.set_mode((1080, 720))

            # Define um nome para a janela
            pygame.display.set_caption("Drag and Drop")

            # Utiliza uma lista para armazenar os herois do jogo
            self.heroes = []

            # Utilizado para controlar a velocidade de quadros (de atualizacoes da tela)
            self.clock = pygame.time.Clock()

        # Funcao utilizada para criar e carregar a imagem de todos os herois
        def create_heroes(self):
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/cabeloM.png", (300, 250), [50, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/cabelo.png", (200, 70), [50, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/olhos.png", (75, 55), [400, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/olhose.png", (75, 55), [600, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/sobrancelhad.png", (40, 25), [800, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/sobrancelhae.png", (40, 25), [1000, 80]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/boca.png", (130, 30), [700, 150]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/bochecha.png", (50, 30), [800, 150]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/bochecha.png", (50, 30), [600, 250]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/braçod.png", (100, 128), [800, 450]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/braçoe.png", (100, 128), [50, 150]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/colar.png", (85, 40), [50, 250]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/maod.png", (100, 60), [50, 350]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/maoe.png", (100, 60), [50, 450]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/nariz.png", (50, 25), [50, 500]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/anel.png", (30, 28), [600, 150]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/cabelod.png", (135, 155), [600, 150]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/cabeloe.png", (135, 155), [600, 300]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/pernad.png", (80, 125), [600, 450]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/pernae.png", (80, 125), [600, 500]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/péd.png", (110, 45), [400, 600]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/pee.png", (110, 45), [500, 600]))
            self.heroes.append(Hero("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/bigode.png", (150, 100), [500, 150]))


        # Funcao utilizada para verificar se a posicao do mouse esta em cima
        # de um heroi (passado por parametro)
        def is_over(self, mouse_pos, hero):
            # Verifica a posicao no eixo X
            if mouse_pos[0] > hero.position[0] and mouse_pos[0] < hero.position[0] + hero.scale[0]:
                # Verifica a posicao no eixo Y
                if mouse_pos[1] > hero.position[1] and mouse_pos[1] < hero.position[1] + hero.scale[1]:
                    return True
            return False

        # Funcao chamada quando o usuario clica com o mouse
        def mouse_button_down(self):
            # Obtem a posicao atual do mouse
            mouse_pos = mouse.get_pos()

            for i in range(0, len(self.heroes)):
                # Somente "ativa" a imagem_selecionada se o usuario clicou em cima da imagem
                if self.is_over(mouse_pos, self.heroes[i]):
                    self.heroes[i].held = True

        # Funcao chamada quando o usuario solta o botao do mouse
        def mouse_button_up(self):
            # 'Libera' todos os herois
            for i in range(0, len(self.heroes)):
                self.heroes[i].held = False

        # Funcao responsavel por atualizar a posicao de todos os herois
        def update_position(self):
            # Obtem a posicao atual do mouse
            mouse_pos = mouse.get_pos()

            for i in range(0, len(self.heroes)):
                # Se a variavel imagem_selecionada estiver "ativa" (True), atualiza a posicao da imagem
                if self.heroes[i].held:
                    # Define as posicoes X e Y da imagem, posiciona a imagem com o mouse centralizado
                    self.heroes[i].position[0] = mouse_pos[0] - self.heroes[i].scale[0]/2
                    self.heroes[i].position[1] = mouse_pos[1] - self.heroes[i].scale[1]/2

        # Funcao que roda o jogo
        def run(self):
            # Chama a funcao para criar os herois
            self.create_heroes()

            # Loop principal do jogo
            while True:

                # Verifica se algum evento aconteceu
                for event in pygame.event.get():
                    # Verifica se foi um evento de saida (pygame.QUIT), em caso afirmativo fecha a aplicacao
                    if event.type == pygame.QUIT: 
                        sys.exit()
                    # Se o usuario soltar o botao do mouse "ativa" a variavel imagem_selecionada
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_button_down()
                    # Se o usuario soltar o botao do mouse "desativa" a variavel imagem_selecionada
                    elif event.type == pygame.MOUSEBUTTONUP:
                        self.mouse_button_up()

                # Chama a funcao que atualiza a posicao dos herois
                self.update_position()
                self.main_window.fill(white)
                # Preenche a tela com uma cor, neste caso preto (definido logo apos importar as bibliotecas)
                img = pygame.image.load (os.path.join ("C:/Users/monitoramento/Downloads/ESTUDO/ESTUDO/fase4/corpo2.png"))
                self.main_window.blit(img, ((200), (50)))
                
                botao("Confirmar", 900, 650, 120, 50, ci = greem, ca = green, acao = "gameLoop")

                # Coloca a imagem de todos os herois na tela com base na posicao
                for i in range(0, len(self.heroes)):
                    self.main_window.blit(self.heroes[i].image, self.heroes[i].position)
                
                # Atualiza a tela visivel ao usuario
                pygame.display.flip()

                # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
                self.clock.tick(60)

    if __name__ == "__main__":
        game = Game()
        game.run()


def erro():
   
    pygame.draw.rect(tela, blue,(355, 195, 300, 200))
    pygame.draw.rect(tela, white,(360, 200, 290, 190))
    texto("Resposta errada!", 504, 440 ) 
    sair = False
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        botao("Menu", 455, 350, 100, 35, ca = blue, ci = blue, acao = "menu")

        pygame.display.update()
    relogio.tick(30)
    
    pygame.quit()


def gameLoop():
    sair = False
    tela.fill( black )
    texto2( "PROGRAMAÇÃO:", (300), (300) )
    texto2( "HUGO FERRARI", (700), (300) )
    texto2( "JULIA LORETTA", (690), (400) )
    texto2( "DOCUMENTAÇÃO:", (300), (650) )
    texto2( "LAURA MILIANE", (700), (650) )
    texto2( "LUANA SANTOS", (700), (750) )
    texto2( "PROF:ORIENTADOR:", (300), (1000) )
    texto2( "JEDERSON ZUCHI", (700), (1000) )
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        botao("MENU", 500, 600, 120, 50, ci = white, ca = white, acao = "menu")
        pygame.display.update()
    relogio.tick( 30 )

    pygame.quit()
menu()