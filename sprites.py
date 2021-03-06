import random
import pygame
from config import WIDTH, HEIGHT, METEOR_WIDTH, METEOR_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT
from assets import SHIP_IMG, PEW_SOUND, METEOR_IMG1, METEOR_IMG2, METEOR_IMG3, METEOR_GRAY, BULLET_IMG, EXPLOSION_ANIM, VIDA_IMG


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[SHIP_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.assets = assets
        self.groups = groups

        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 250

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now

            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet = Bullet(self.assets, self.rect.right, self.rect.centery)
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_bullets'].add(new_bullet)
            self.assets[PEW_SOUND].play()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        meteoro_marrom_diferentes = [METEOR_IMG1, METEOR_IMG2, METEOR_IMG3]
        self.image = assets[random.choice(meteoro_marrom_diferentes)]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH+METEOR_WIDTH)
        y_nasce_meteoro = [10, 150, 280, 410, 540]
        self.rect.y = random.choice((y_nasce_meteoro))
        self.speedy = 0

        velocidade_possibilidades = random.randint(0,10)
        if velocidade_possibilidades <= 8:
            self.speedx = random.randint(4, 10)
        elif velocidade_possibilidades > 8:
            self.speedx = random.randint(22, 28)
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.left<-METEOR_WIDTH or self.rect.top<-METEOR_HEIGHT or self.rect.bottom>(HEIGHT+METEOR_HEIGHT) or self.rect.right>(WIDTH+METEOR_WIDTH+15):
            self.rect.x = random.randint(WIDTH, WIDTH+METEOR_WIDTH)
            y_nasce_meteoro = [10, 150, 280, 410, 540]
            self.rect.y = random.choice((y_nasce_meteoro))
            self.speedy = 0
            velocidade_possibilidades = random.randint(0,10)
            if velocidade_possibilidades <= 8:
                self.speedx = random.randint(4, 10)
            elif velocidade_possibilidades > 8:
                self.speedx = random.randint(22, 28)
class MeteorGRAY(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[METEOR_GRAY]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH+METEOR_HEIGHT)
        y_nasce_meteoro = [10, 150, 280, 410, 540]
        self.rect.y = random.choice((y_nasce_meteoro))
        self.speedy = 0
        velocidade_possibilidades = random.randint(0,10)
        if velocidade_possibilidades <= 8:
            self.speedx = random.randint(4, 10)
        elif velocidade_possibilidades > 8:
            self.speedx = random.randint(22, 28)
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.left<-METEOR_WIDTH or self.rect.top<-METEOR_HEIGHT or self.rect.bottom>(HEIGHT+METEOR_HEIGHT) or self.rect.right>(WIDTH+METEOR_WIDTH+15):
            self.rect.x = random.randint(WIDTH, WIDTH+METEOR_HEIGHT)
            y_nasce_meteoro = [10, 150, 280, 410, 540]
            self.rect.y = random.choice((y_nasce_meteoro))
            self.speedy = 0
            velocidade_possibilidades = random.randint(0,10)
            if velocidade_possibilidades <= 8:
                self.speedx = random.randint(4, 10)
            elif velocidade_possibilidades > 8:
                self.speedx = random.randint(22, 28)
                
class item_vida(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[VIDA_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, 7200)
        self.rect.y = random.randint(10, HEIGHT-50)
        self.speedy = 0
        self.speedx = random.randint(0, 20)
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        # novas posições e velocidades
        if self.rect.left<-76 or self.rect.top<-64 or self.rect.bottom>(HEIGHT+64):
            self.rect.x = random.randint(WIDTH, 4800)
            self.rect.y = random.randint(10, HEIGHT-50)
            self.speedy = 0
            self.speedx = random.randint(0, 20)


# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, right, centery):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[BULLET_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centery = centery
        self.rect.right = right
        self.speedx = 16  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.right > WIDTH:
            self.kill()

# Classe que representa uma explosão de meteoro
class Explosion(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = assets[EXPLOSION_ANIM]

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
