import pygame 
from settings import SCREEN_HEIGHT, DAMAGE


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/images/player.png').convert_alpha()
        self.rect = self.image.get_rect(centre=(x, y))
        self.vel_y = 0
        self.hp

    def update(self, keys):
        #Gravity
        self.vel_y += 0.5
        self.rect.y += self.vel_y

        #jump
        if keys[pygame.K_SPACE] and self.rect.bottom >= SCREEN_HEIGHT - 10:
            self.vel_y = -15

        #move left/right
        if keys[pygame.K_LEFT]:
            self.rect.x -=5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

    def take_damage(self):
        self.hp -= DAMAGE
        if self.hp <=0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/images/enemy.png').convert_alpha()
        self.rect = self.image.get_rect(centre=(x, y))

    def shoot(self, projectile_group):
        bullet = Projectile(self.rect,centrex,self.rect.bottom)
        projectile_group.add(bullet)



class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
         self.image = pygame.Surface((10, 10))
         self.image.fill(RED)
         self.rect = self.image.get_rect(center=(x, y))

    def update(self):
            self.rect.y +=5

            if self.rect.top > SCREEN_HEIGHT:
                self.kill()

class FlamingBall(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x, vel_y):
        super()._init__()
        self.image = pygame.Surface((20,20))
        self.image.fill((255,100,0))
        self.rect = self.image.get_rect(centre=(x,y))
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        #remove the ball if it goes off-screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
