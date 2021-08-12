import pygame
import random
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED
from assets import load_assets, DESTROY_SOUND, BOOM_SOUND, BACKGROUND, SCORE_FONT
from sprites import Ship, Meteor, Bullet, MeteorGRAY, Explosion


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    all_meteors = pygame.sprite.Group()

    brown_meteors = pygame.sprite.Group()
    gray_meteors = pygame.sprite.Group()

    groups = {}

    groups['all_sprites'] = all_sprites
    groups['all_bullets'] = all_bullets
    groups['all_meteors'] = all_meteors

    groups['brown_meteors'] = brown_meteors
    groups['gray_meteors'] = gray_meteors


    # Criando o jogador
    player = Ship(groups, assets)
    all_sprites.add(player)

    for i in range(1):
        meteor = MeteorGRAY(assets)
        all_sprites.add(meteor)
        all_meteors.add(meteor)
        gray_meteors.add(meteor)

    # Criando os meteoros
    for i in range(3):
        meteor = Meteor(assets)
        all_sprites.add(meteor)
        all_meteors.add(meteor)
        brown_meteors.add(meteor)

    x0 = 0
    x1 = WIDTH
    fundo = assets[BACKGROUND]
    fundo_rect = fundo.get_rect()

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    #Movimentação é controlada pela VELOCIDADE
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 9
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 6
                    if event.key == pygame.K_SPACE:
                        player.shoot()
                    if event.key == pygame.K_UP:
                        player.speedy -= 7
                    if event.key == pygame.K_DOWN:
                        player.speedy += 7
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 9
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 6
                        if event.key == pygame.K_UP:
                            player.speedy += 7
                        if event.key == pygame.K_DOWN:
                            player.speedy -= 7
        
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre tiro e meteoro
            hits = pygame.sprite.groupcollide(all_meteors, all_bullets, True, True, pygame.sprite.collide_mask)
            for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                assets[DESTROY_SOUND].play()

                novo_meteoro_prob = random.randint(0,10)
                if novo_meteoro_prob <= 7:
                    meteor = Meteor(assets)
                    all_sprites.add(meteor)
                    all_meteors.add(meteor)
                    brown_meteors.add(meteor)

                elif novo_meteoro_prob > 7:
                    meteor = MeteorGRAY(assets)
                    all_sprites.add(meteor)
                    all_meteors.add(meteor)
                    gray_meteors.add(meteor)

                # No lugar do meteoro antigo, adicionar uma explosão.
                explosao = Explosion(meteor.rect.center, assets)
                all_sprites.add(explosao)

                # Ganhou pontos!
                score += 200
                if score % 1000 == 0:
                    for i in range(1):                   
                        meteor = Meteor(assets)
                        all_sprites.add(meteor)
                        all_meteors.add(meteor)
                        brown_meteors.add(meteor)

                if score % 3000 == 0:
                    for i in range(1):                   
                        meteor = MeteorGRAY(assets)
                        all_sprites.add(meteor)
                        all_meteors.add(meteor)
                        gray_meteors.add(meteor)

            # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, brown_meteors, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
              # Verifica se houve colisão entre nave e meteoro
            hits = pygame.sprite.spritecollide(player, gray_meteors, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                lives -= 2
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                state = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400

        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives <= 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Ship(groups, assets)
                    all_sprites.add(player)

        #Gera saídas
        ############
        window.fill(BLACK)  
        window.blit(fundo, fundo_rect)

        window.blit(fundo, (x0, 0))
        window.blit(fundo, (x1, 0))


        x0 -= 5
        x1 -= 5

        if x0 <= -WIDTH:
            x0 = WIDTH
            pygame.display.flip()
        if x1 <= -WIDTH:
            x1 = WIDTH  
            pygame.display.flip()


        # Desenhando meteoros
        all_sprites.draw(window) 

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
