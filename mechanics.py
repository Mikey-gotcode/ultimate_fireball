import pygame

def apply_gravity(sprite, gravity=0.5, terminal_velocity=10):
        """
        Applies gravity to a given sprite.
        :param sprite: The sprite object (must have `vel_y` and `rect.y` attributes)                :param gravity: The acceleration due to gravity.
        :param terminal_velocity: The maximum speed due to gravity.
                            """
        sprite.vel_y = min(sprite.vel_y + gravity, terminal_velocity)
        sprite.rect.y += sprite.vel_y


def handle_platform_collisions(player, platforms):
                                            """
        Handles collisions between the player and platforms.
        Ensures the player lands on platforms and doesn't fall through.
        :param player: The player sprite.
        :param platforms: A group of platform sprites.
                                                                """
        collisions = pygame.sprite.spritecollide(player, platforms, False)
        if collisions:
            for platform in collisions:
                                                                                                    
                # Check if the player is falling and collides from above the platform
                if player.vel_y > 0 and player.rect.bottom <= platform.rect.top + 10                          
                   player.rect.bottom = platform.rect.top
                   player.vel_y = 0  # Stop vertical movement
                   break

def check_boundary_loss(player, screen_height):
                                                                                                                                                                        """
Checks if the player has fallen off the screen (losing condition).
:param player: The player sprite.
:param screen_height: The height of the game screen.
                                                                                                                                                                        :return: True if the player is off the screen, False otherwise.
                                                                                                                                                                                            """
                                                                                                                                                                                return player.rect.top > screen_height


                                                                                                                                                                                    
                                                                                                                                                                        def handle_projectile_collisions(player, projectiles, sound_effect):
                                                                                                                                                                                                    """
                                                                                                                                                                        Handles collisions between the player and projectiles (or flaming balls).
                                                                                                                                                                        :param player: The player sprite.
                                                                                                                                                                        :param projectiles: A group of projectile sprites.
                                                                                                                                                                        :param sound_effect: The sound to play on hit.
                                                                                                                                                                                                                        """
                                                                                                                                                                                hits = pygame.sprite.spritecollide(player, projectiles, True)  # True removes the projectile
                                                                                                                                                                                if hits:
                                                                                                                                                                                   player.take_damage()
                                                                                                                                                                                   sound_effect.play()


                                                                                                                                                                        def generate_flaming_balls(ball_group, screen_width, screen_height, ball_frequency):
                                                                                                                                                                                                                                                            """
                                                                                                                                                                        Generates flaming balls from the sides of the screen at random intervals.
                                                                                                                                                                        :param ball_group: The group to which flaming balls are added.
                                                                                                                                                                        :param screen_width: Width of the game screen.
                                                                                                                                                                        :param screen_height: Height of the game screen.
                                                                                                                                                                        :param ball_frequency: Number of flaming balls to generate per second.
                                                                                                                                                                                                                                                                                    """
                                                                                                                                                            
                                                                                                                                                                         
                                                                                                                                                                        import random
                                                                                                                                                                        if random.randint(1, 60) <= ball_frequency:  # Assuming FPS = 60
                                                                                                                                                                        side = random.choice(['left', 'right'])
                                                                                                                                                                        y_position = random.randint(0, screen_height - 50)
                                                                                                                                                                        if side == 'left':
                                                                                                                                                                        ball = FlamingBall(-20, y_position, 5, 0)  # Ball moves right
                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                        ball = FlamingBall(screen_width + 20, y_position, -5, 0)  # Ball moves left
                                                                                                                                                                        ball_group.add(ball)

