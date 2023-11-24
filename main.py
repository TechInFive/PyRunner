import pygame
import sys
from Background import Background
from ObstacleManager import ObstacleManager
from Player import Player

from constants import FONT_COLOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyRunner")
font = pygame.font.Font(None, 36)  # Default font with size 36

def game_over_screen(score):
    screen.fill((255, 255, 255))  # White background
    game_over_text = font.render("Game Over!", True, FONT_COLOR)
    score_text = font.render(f"Final Score: {score}", True, FONT_COLOR)
    restart_text = font.render("Press 'R' to Restart or 'Q' to Quit", True, FONT_COLOR)

    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 150))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 250))

    pygame.display.flip()

    # Wait for player input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # Restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    clock = pygame.time.Clock()
    player = Player()
    background = Background()
    obstacle_manager = ObstacleManager()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        obstacle_manager.generate_obstacle()
        obstacle_manager.update_obstacles()
        background.update()
        player.update()

        # Check for collision
        for obstacle in obstacle_manager.obstacles[:]:
            if player.get_rect().colliderect(obstacle.get_rect()):
                game_over_screen(score)  # Handle game over

        # Update score
        score += 1

        screen.fill((255, 255, 255))  # White background
        background.draw(screen)
        obstacle_manager.draw_obstacles(screen)
        player.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, FONT_COLOR)
        screen.blit(score_text, (10, 10))  # Position the score in the top-left corner

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
