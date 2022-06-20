import pygame
import random

# ESSENTIAL!!
# Reset
pygame.init()

# Screen size setting
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 480
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game title
pygame.display.set_caption("똥 피하기 게임")

# FPS(Frames Per Second)
clock = pygame.time.Clock()

######################################################################################################

# User reset

# Background
background \
    = pygame.image.load("images/background.png")


# Player sprite
player \
    = pygame.image.load("images/player.png")
player_size = player.get_rect().size  # Player size
player_width = player_size[0]
player_height = player_size[1]
# Player first x position : Center of Screen
player_x_position = (SCREEN_WIDTH / 2) - (player_width / 2)
# Player first y position : Bottom of Screen
player_y_position = SCREEN_HEIGHT - player_height

# Player speed
player_speed = 0.7

# Position to move
to_x = 0


# Poop
poop \
    = pygame.image.load("images/poop.png")
poop_size = poop.get_rect().size  # Poop size
poop_width = poop_size[0]
poop_height = poop_size[1]
# Poop first x position : random
poop_x_position = random.randint(0, (SCREEN_WIDTH - poop_width))
# Poop first y position : Top of Screen
poop_y_position = 0

# Poop speed
poop_speed = 30


# Game font setting (style, size)
game_font \
    = pygame.font.Font("font/DungGeunMo.ttf", 50)

# Total play time
total_time = 100

# Start play time
start_ticks = pygame.time.get_ticks()  # Current ticks
