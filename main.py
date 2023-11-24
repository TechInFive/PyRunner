import pygame
import sys
from Background import Background
from Player import Player

from constants import FONT_COLOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyRunner")

def main():
    clock = pygame.time.Clock()
    player = Player()
    background = Background()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        background.update()
        player.update()

        screen.fill((255, 255, 255))  # White background
        background.draw(screen)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
