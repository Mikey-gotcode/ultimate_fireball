import pygame
from settings import *
from entities import Player, Enemy, Projectile
from platform import Platform
from menu import main_menu

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.mixer.init()
hit_sound = pygame.mixer.Sound('assets/audio/got_hit.mp3')

# Main Game Loop
def game():
        difficulty = main_menu(screen)
        player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        platforms = Platform.generate_platforms(10)
        enemies = pygame.sprite.Group(Enemy(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        projectiles = pygame.sprite.Group()
        running = True
        
        while running:
            screen.fill(BLACK)
            keys = pygame.key.get_pressed()

            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            
            # Game Logic
            player.update(keys)
            projectiles.update()

            
            # Check Collisions
            if pygame.sprite.spritecollide(player, projectiles, True):
                player.take_damage()
                hit_sound.play()

                                                                                                                                                                                    # Draw everything
                                                                                                                                                                                    platforms.draw(screen)
                                                                                                                                                                                    projectiles.draw(screen)
                                                                                                                                                                                    enemies.draw(screen)
                                                                                                                                                                                    screen.blit(player.image, player.rect)

                                                                                                                                                                                    pygame.display.flip()
                                                                                                                                                                                    clock.tick(FPS)

                                                                                                                                                                                    pygame.quit()

                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                    game()
                                                                                                                                                                                                                                                
