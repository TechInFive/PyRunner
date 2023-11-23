
import pygame

from constants import SCREEN_HEIGHT

INITIAL_SPEED =  20  # Initial speed of the jump
GRAVITY = 1  # Gravity effect

SCALE = 3
PLAYER_HEIGHT = 60 * SCALE
PLAYER_WIDTH = 60 * SCALE
HEAD_RADIUS = 10 * SCALE
BODY_LENGTH = 20 * SCALE
ARM_LENGTH = 20 * SCALE
LEG_LENGTH = 20 * SCALE

START_POS_X = 100  # Starting x-position
START_POS_Y = SCREEN_HEIGHT - PLAYER_HEIGHT  # Start on the ground

class Player:
    def __init__(self):
        self.height = PLAYER_HEIGHT
        self.width = PLAYER_WIDTH
        self.x = START_POS_X
        self.y = START_POS_Y
        self.jump_speed = INITIAL_SPEED
        self.is_jumping = False
        self.velocity = 0

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity = -self.jump_speed

    def update(self):
        # If the player is jumping, apply gravity
        if self.is_jumping:
            self.y += self.velocity
            self.velocity += GRAVITY

            # Check if the player has landed
            if self.y >= SCREEN_HEIGHT - self.height:
                self.y = SCREEN_HEIGHT - self.height
                self.is_jumping = False

    def get_rect(self):
        # Return the current bounding box of the player
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
       head_center = (self.x + self.width // 2, self.y + HEAD_RADIUS)
       body_start = (head_center[0], head_center[1] + HEAD_RADIUS)
       body_end = (body_start[0], body_start[1] + BODY_LENGTH)
       arm_start = body_start
       arm_end = (body_start[0], body_start[1] + ARM_LENGTH)
       leg_start = body_end
       leg_end = (body_end[0], body_end[1] + LEG_LENGTH)

       # Draw the head (circle)
       pygame.draw.circle(screen, (0, 0, 0), head_center, HEAD_RADIUS)
       pygame.draw.circle(screen, (255, 255, 255), head_center, HEAD_RADIUS - 2)  # White fill
       # Draw the body (line)
       pygame.draw.line(screen, (0, 0, 0), body_start, body_end, 2)
       # Draw the arms (lines)
       pygame.draw.line(screen, (0, 0, 0), arm_start, (arm_end[0] - ARM_LENGTH, arm_end[1]), 2)
       pygame.draw.line(screen, (0, 0, 0), arm_start, (arm_end[0] + ARM_LENGTH, arm_end[1]), 2)
       # Draw the legs (lines)
       pygame.draw.line(screen, (0, 0, 0), leg_start, (leg_end[0] - LEG_LENGTH // 2, leg_end[1]), 2)
       pygame.draw.line(screen, (0, 0, 0), leg_start, (leg_end[0] + LEG_LENGTH // 2, leg_end[1]), 2)


