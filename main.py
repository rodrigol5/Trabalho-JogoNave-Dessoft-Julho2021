#===INICIALIZA===
import pygame
import random

from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen

#Esse arquivo contêm o LOOP PRINCIPAL DO PYGAME.
#Esse arquivo contem o código que INICIALIZA/CHAMA O PYGAME.

pygame.init() #Inicia o jogo visualmente
pygame.mixer.init() #Inicia som/audio do jogo

#===GERA JANELA===
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

#===LOOP PRINCIPAL===
state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

#===FINALIZA JOGO===
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados




