from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# TELA DO JOGO
WIDTH = 1600 #Largura da tela
HEIGHT = 720 #Altura da tela

# FRAMES 
FPS = 60 

# ESTADOS DE FLUXO
INIT = 0 #init_screen
GAME = 1 #game_screen
QUIT = 2 #pygame.quit

# TAMANHOS DA NAVE + METEOROS
METEOR_WIDTH = 50
METEOR_HEIGHT = 38
SHIP_WIDTH = 50
SHIP_HEIGHT = 38

# PALHETTA DE CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

