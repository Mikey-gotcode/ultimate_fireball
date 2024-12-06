import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

def main_menu(screen):
        font = pygame.font.Font(None, 74)
        title = font.render('Game Menu', True, WHITE)
        easy_button = font.render('Easy', True, WHITE)
        hard_button = font.render('Hard', True, WHITE)

        while True:
            screen.fill((0, 0, 0))
            screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))
            screen.blit(easy_button, (SCREEN_WIDTH // 2 - easy_button.get_width() // 2, 200))
            screen.blit(hard_button, (SCREEN_WIDTH // 2 - hard_button.get_width() // 2, 300))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.get_rect(center=(SCREEN_WIDTH // 2, 200)).collidepoint(event.pos):
                                                                                                                                                                                        return 'easy'
                                                                                                                            
                if hard_button.get_rect(center=(SCREEN_WIDTH // 2, 300)).collidepoint(event.pos):    

                return 'hard'
                                                                                                                                                                                                                
