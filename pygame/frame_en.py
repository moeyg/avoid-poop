import pygame

######################################################################################################

# ESSENTIAL!!!
# Reset
pygame.init()

# Screen size
screen_width = 480  # horizontal
screen_height = 640  # vertical
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen caption
pygame.display.set_caption("game_name")

# Frames Per Second(FPS)
clock = pygame.time.Clock()

######################################################################################################

# 1. User Game Reset - Background, Game images, Position(coordinate), Speed, Font ... etc

# Load background image
background = pygame.image.load(
    "images/background.png")

# Load sprite(player)
player = pygame.image.load(
    "images/player.png")
player_size = player.get_rect().size  # Image size
player_width = player_size[0]  # player row size
player_height = player_size[1]  # player column size
# Located at the center of the screen -> horizontal position
player_x_position = (screen_width / 2) - (player_width / 2)
# Located at the bottom of the screen -> vertical position
player_y_position = screen_height - player_height

# Position to move
to_x = 0
to_y = 0

# player move speed
player_speed = 0.5

# obstacle
obstacle = pygame.image.load(
    "images/obstacle.png")
obstacle_size = obstacle.get_rect().size  # Image size
obstacle_width = obstacle_size[0]  # obstacle row size
obstacle_height = obstacle_size[1]  # obstacle column size
# Located at the center of the screen -> horizontal position
obstacle_x_position = (screen_width / 2) - (obstacle_width / 2)
# Located at the center of the screen -> vertical position
obstacle_y_position = (screen_height / 2) - obstacle_height

# Font
# Creat font(style, size)
game_font = \
    pygame.font.Font(
        "font/game_font.ttf", 40)

# Total time
total_time = 10

# Start time
start_ticks = pygame.time.get_ticks()  # Download current ticks

# Event loop
running = True  # game running
while running:
    delta = clock.tick(30)  # FPS

######################################################################################################

    # 2. Event handling : Keyboard, Mouse ... etc

    for event in pygame.event.get():  # Event occurrence list
        if event.type == pygame.QUIT:  # X-box button click event
            running = False  # Not in progress

        if event.type == pygame.KEYDOWN:  # Check key pressed event
            if event.key == pygame.K_LEFT:  # Move Player left
                to_x -= player_speed
            elif event.key == pygame.K_RIGHT:  # Move Player right
                to_x += player_speed
            elif event.key == pygame.K_UP:  # Move Player up
                to_y -= player_speed
            elif event.key == pygame.K_DOWN:  # Move Player down
                to_y += player_speed

        if event.type == pygame.KEYUP:  # Stop Player move when no key pressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

######################################################################################################

    # 3. player position setting

    player_x_position += to_x * delta
    player_y_position += to_y * delta

    # Horizontal boundary value handling
    if player_x_position < 0:
        player_x_position = 0
    elif player_x_position > screen_width - player_width:
        player_x_position = screen_width - player_width

    # Vertical boundary value handling
    if player_y_position < 0:
        player_y_position = 0
    elif player_y_position > screen_height - player_height:
        player_y_position = screen_height - player_height

######################################################################################################

    # 4. Images collision check handling

    # Rect information update for collision handling
    # Player rect
    player_rect = player.get_rect()
    player_rect.left = player_x_position
    player_rect.top = player_y_position
    # Obstacle rect
    obstacle_rect = obstacle.get_rect()
    obstacle_rect.left = obstacle_x_position
    obstacle_rect.top = obstacle_y_position

    # Collision handling
    if player_rect.colliderect(obstacle_rect):
        running = False

######################################################################################################

    # 5. Game time setting

    # Timer
    # Calculate elapsed time
    elapsed_time \
        = (pygame.time.get_ticks() - start_ticks) / 1000  # (Current ticks - Start ticks) / 1000
    timer \
        = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))  # Print value, True, color
    # Time out
    if total_time - elapsed_time <= 0:
        print("Time Out!!!")
        running = False

######################################################################################################

    # 6. Draw element

    screen.blit(background, (0, 0))  # Creat background
    screen.blit(player,
                (player_x_position, player_y_position))  # Creat player
    screen.blit(obstacle,
                (obstacle_x_position, obstacle_y_position))  # Creat obstacle
    screen.blit(timer, (425, 10))  # Creat timer

    pygame.display.update()  # Redraw game screen - ESSENTIAL!!

######################################################################################################

# Time out 2s waiting
pygame.time.delay(1500)

# Game quit
pygame.quit()
