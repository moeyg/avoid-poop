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
    = pygame.image.load("/Users/moeyg/Desktop/PhythonWorkspace/pygame/avoid_poop/images/background.png")


# Player sprite
player \
    = pygame.image.load("/Users/moeyg/Desktop/PhythonWorkspace/pygame/avoid_poop/images/player.png")
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
    = pygame.image.load("/Users/moeyg/Desktop/PhythonWorkspace/pygame/avoid_poop/images/poop.png")
poop_size = poop.get_rect().size  # Poop size
poop_width = poop_size[0]
poop_height = poop_size[1]
# Poop first x position : random
poop_x_position = random.randint(0, (SCREEN_WIDTH - poop_width))
# Poop first y position : Top of Screen
poop_y_position = 0

# Poop speed
poop_speed = 20


# Game font setting (style, size)
game_font \
    = pygame.font.Font("/Users/moeyg/Desktop/PhythonWorkspace/pygame/avoid_poop/font/DungGeunMo.ttf", 50)

# Total play time
total_time = 100

# Start play time
start_ticks = pygame.time.get_ticks()  # Current ticks

######################################################################################################

# Game loop

run = True
while run:
    fps = clock.tick(30)  # FPS

    # Event loop
    # Event occurrence list
    for event in pygame.event.get():
        # X-Box button click event
        if event.type == pygame.QUIT:
            run = False  # Game quit

        # Key press event
        if event.type == pygame.KEYDOWN:
            # Move to left
            if event.key == pygame.K_LEFT:
                to_x -= player_speed
            # Move to right
            elif event.key == pygame.K_RIGHT:
                to_x += player_speed

        # Key non-press event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0  # Stop move

    # Position setting

    # Player position setting
    player_x_position += to_x * fps
    # Player horizontal boundary value handling
    if player_x_position < 0:
        player_x_position = 0
    elif player_x_position > SCREEN_WIDTH - player_width:
        player_x_position = SCREEN_WIDTH - player_width

    # Poop position setting
    poop_y_position += poop_speed
    # Poop vertical boundary value handling
    if poop_y_position > SCREEN_HEIGHT:
        poop_y_position = 0
        poop_x_position = random.randint(0, (SCREEN_WIDTH - poop_width))

######################################################################################################

    # Handling collisions between images

    # Rect info update
    # Player rect info update
    player_rect = player.get_rect()
    player_rect.left = player_x_position
    player_rect.top = player_y_position

    # Poop rect info update
    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_position
    poop_rect.top = poop_y_position

    # Handling collisions
    if player_rect.colliderect(poop_rect):
        run = False  # Game quit

######################################################################################################

    # Game time setting

    # Timer
    # Calculate elapsed time
    elapsed_time \
        = (pygame.time.get_ticks() - start_ticks) / 1000  # (Current ticks - Start ticks) / 1000
    timer \
        = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))  # Print value, True, color
    # Time Out
    if total_time - elapsed_time <= 0:
        print("Time Out!!!")
        running = False

######################################################################################################

    # Draw element

    SCREEN.blit(background, (0, 0))  # Creat background
    SCREEN.blit(player, (player_x_position, player_y_position))  # Creat player
    SCREEN.blit(poop, (poop_x_position, poop_y_position))  # Creat poop
    SCREEN.blit(timer, (340, 10))  # Creat timer

    pygame.display.update()  # Redraw game screen - ESSENTIAL!!

######################################################################################################

# Time out delay
pygame.time.delay(2000)

# Game quit
pygame.quit()
