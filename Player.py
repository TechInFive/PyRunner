
import math
import pygame

from constants import SCREEN_HEIGHT

INITIAL_SPEED =  20  # Initial speed of the jump
GRAVITY = 1  # Gravity effect

SCALE = 3
PLAYER_HEIGHT = 60 * SCALE
PLAYER_WIDTH = 30 * SCALE
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
        self.run_state = 0  # Current state of the running animation
        self.state_change_timer = 0  # Timer to control state changes

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

        # Update the run state for animation
        self.state_change_timer += 1
        if self.state_change_timer > 10:  # Change state every 10 frames
            self.run_state = (self.run_state + 1) % 4  # Toggle between 0, 1, 2, and 3
            self.state_change_timer = 0

    def get_rect(self):
        # Return the colliderect bounding box of the player
        return pygame.Rect(self.x  + self.width // 2, self.y, self.width // 2, self.height)

    def draw_circle(self, screen, center, radius):
        pygame.draw.circle(screen, (0, 0, 0), center, radius)
        pygame.draw.circle(screen, (255, 255, 255), center, radius - 2)

    def draw_line(self, screen, start, length, angle):
        # Convert angle from degrees to radians for math functions
        angle_rad = math.radians(angle)
        
        # Calculate the end point of the line
        end_x = start[0] + (length * math.cos(angle_rad))
        end_y = start[1] + (length * math.sin(angle_rad))
        end_point = (end_x, end_y)
        
        # Draw the line on the screen
        pygame.draw.line(screen, (0, 0, 0), start, end_point, 2)
        return end_point
    
    def draw_arm(self, screen, arm_start, angle_1, angle_2):
        elbow = self.draw_line(screen, arm_start, ARM_LENGTH // 2, angle_1)
        hand = self.draw_line(screen, elbow, ARM_LENGTH // 2, angle_2)
        self.draw_circle(screen, hand, 4)

    def draw_leg(self, screen, leg_start, angle_1, angle_2):
        knee = self.draw_line(screen, leg_start, LEG_LENGTH // 2, angle_1)
        foot = self.draw_line(screen, knee, LEG_LENGTH // 2, angle_2)
        self.draw_line(screen, foot, 10, 0)

    def draw(self, screen):
        head_center = (self.x + self.width // 2, self.y + HEAD_RADIUS)
        body_start = (head_center[0], head_center[1] + HEAD_RADIUS)
        body_end = (body_start[0], body_start[1] + BODY_LENGTH)
        arm_start = body_start
        leg_start = body_end

        # Draw the head
        self.draw_circle(screen, head_center, HEAD_RADIUS)
        # Draw the body
        self.draw_line(screen, body_start, BODY_LENGTH, 90)
   
        # Define the keyframe states of the walking cycle
        if self.run_state == 0:  # Contact
            self.draw_arm(screen, arm_start, 160, 100)
            self.draw_arm(screen, arm_start, 40, 340)
            self.draw_leg(screen, leg_start, 110, 120)
            self.draw_leg(screen, leg_start, 30, 50)
        elif self.run_state == 1:  # Down
            self.draw_arm(screen, arm_start, 140, 70)
            self.draw_arm(screen, arm_start, 60, 350)
            self.draw_leg(screen, leg_start, 90, 140)
            self.draw_leg(screen, leg_start, 50, 70)
        elif self.run_state == 2:  # Passing
            self.draw_arm(screen, arm_start, 120, 50)
            self.draw_arm(screen, arm_start, 80, 10)
            self.draw_leg(screen, leg_start, 70, 160)
            self.draw_leg(screen, leg_start, 70, 90)
        elif self.run_state == 3:  # Up
            self.draw_arm(screen, arm_start, 100, 30)
            self.draw_arm(screen, arm_start, 100, 30)
            self.draw_leg(screen, leg_start, 50, 120)
            self.draw_leg(screen, leg_start, 90, 110)



