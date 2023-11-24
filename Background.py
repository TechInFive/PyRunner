import random

import pygame

from constants import BG_SCROLL_SPEED, CANOPY_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, TRUNK_HEIGHT

class Background:
    def __init__(self):
        self.scroll_speed = BG_SCROLL_SPEED
        self.trees = []  # List to store the position of each tree
        self.generate_trees()

    def generate_trees(self):
        # Create trees with random spacing to simulate background scrolling
        position = 0
        while position < SCREEN_WIDTH:
            # Random space between trees
            space = random.randint(200, 300)  # Random spacing between 100 and 200 pixels
            position += space
            self.trees.append(position)

    def update(self):
        # Move trees to the left
        self.trees = [x - self.scroll_speed for x in self.trees]

        # Loop trees back to the right side
        for i, tree in enumerate(self.trees):
            if tree < 0:
                # Place the tree back to the right with random space
                space = random.randint(200, 300)
                self.trees[i] = SCREEN_WIDTH + space

    def draw(self, screen):
        trunk_top = SCREEN_HEIGHT - TRUNK_HEIGHT
        trunk_bottom = SCREEN_HEIGHT
        tree_top = trunk_top - CANOPY_HEIGHT

        for tree in self.trees:
            # Draw the trunk of the tree
            pygame.draw.line(screen, (139, 69, 19), (tree, trunk_top), (tree, trunk_bottom), 4)
            # Draw the canopy of the tree
            canopy_vertices = [(tree, tree_top),  # Top center
                               (tree - CANOPY_HEIGHT / 4, trunk_top),  # Bottom left
                               (tree + CANOPY_HEIGHT / 4, trunk_top)]  # Bottom right
            pygame.draw.polygon(screen, (34, 139, 34), canopy_vertices)
