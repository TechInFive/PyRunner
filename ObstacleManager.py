import random

from Obstacle import Obstacle
from constants import SCREEN_WIDTH

MAX_OBSTACLES = 5  # Maximum number of obstacles allowed at a time
MIN_DISTANCE = 200  # Minimum distance from the last obstacle

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        if len(self.obstacles) >= MAX_OBSTACLES:
            return  # Do not generate more obstacles if the maximum is reached

        if self.obstacles and (SCREEN_WIDTH - self.obstacles[-1].x < MIN_DISTANCE):
            return  # Do not generate a new obstacle if the last one is too close

        # Randomly decide whether to generate a new obstacle
        if random.randint(0, 1000) < 10:  # 1% chance to generate an obstacle
            self.obstacles.append(Obstacle())

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.x < -obstacle.width:  # Remove obstacle if it's off-screen
                self.obstacles.remove(obstacle)

    def draw_obstacles(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
