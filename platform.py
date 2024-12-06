import pygame
import random 
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/images/platform.png').convert_alpha()
        self.react = self.image.get_rect(centre=(x, y)


    @staticmethod
    def generate_platforms(num_platforms):
        platforms = pygame.sprite.Group()
        for _ in range(num_platforms):
            x = random.randInt(0, SCREEN_HEIGHT - 50)
            y = random.randInt(0, SCREEN_HEIGHT - 50)
            platform.add(Platform(x,y))

        return platforms
