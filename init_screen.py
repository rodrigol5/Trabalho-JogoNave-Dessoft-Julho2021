import pygame
import random
import time
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    background_rect = background.get_rect()

    font = pygame.font.SysFont(None, 100)
    text = font.render('Pressione qualquer tecla', True, (255, 255, 255))

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
                #
            if event.type == pygame.KEYUP:
                state = GAME
                running = False
                #Começa o jogo e sai do init_screen

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        screen.blit(background, background_rect)
        pygame.display.flip()
        time.sleep(1)
        
        screen.blit(text, (50, 590))
        pygame.display.flip()
        time.sleep(1)

    return state


