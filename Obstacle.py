import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

OBSTACLE_SIZE = 50  # Size of obstacles
OBSTACLE_SPEED = 4  # Speed at which obstacles move

class Obstacle:
    def __init__(self):
        self.width = OBSTACLE_SIZE
        self.height = OBSTACLE_SIZE
        self.x = SCREEN_WIDTH  # Start off-screen to the right
        self.y = SCREEN_HEIGHT - self.height  # Align with the ground

    def update(self):
        # Move the obstacle to the left
        self.x -= OBSTACLE_SPEED

    def get_rect(self):
        # Return the current bounding box of the obstacle
        return pygame.Rect(self.x - self.width // 2, self.y, self.width // 2, self.height)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y + self.height // 2), self.width // 2)
