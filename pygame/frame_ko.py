import pygame

######################################################################################################

# 필수적인 부분
# 기본 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("게임_이름")

# 1초 동안 화면 프레임 설정
clock = pygame.time.Clock()

######################################################################################################

# 1. 사용자 초기화 : 배경 화면, 게임 이미지, 좌표, 속도, 폰트 등

# 배경 이미지 불러오기
background = pygame.image.load(
    "images/background.png")

# 플레이어(스프라이트) 불러오기
player = pygame.image.load(
    "images/player.png")
player_size = player.get_rect().size  # 플레이어 이미지 사이즈
player_width = player_size[0]  # 플레이어 가로 길이
player_height = player_size[1]  # 플레이어 세로 길이
# 화면 중앙에 위치 -> 가로 방향
player_x_position = (screen_width / 2) - (player_width / 2)
# 화면 하단에 위치 -> 세로 방향
player_y_position = screen_height - player_height

# 이동할 좌표
to_x = 0
to_y = 0

# 플레이어 움직임 속도
player_speed = 0.5

# 장애물
obstacle = pygame.image.load(
    "images/obstacle.png")
obstacle_size = obstacle.get_rect().size  # 장애물 이미지 사이즈
obstacle_width = obstacle_size[0]  # 장애물 가로 사이즈
obstacle_height = obstacle_size[1]  # 장애물 세로 사이즈
# 화면 정중앙에 위치 -> 가로 방향
obstacle_x_position = (screen_width / 2) - (obstacle_width / 2)
# 화면 정중앙에 위치 -> 세로 방향
obstacle_y_position = (screen_height / 2) - obstacle_height

# 폰트 정의(폰트 스타일, 폰트 사이즈)
game_font = \
    pygame.font.Font(
        "font/game_font.ttf", 40)

# 게임 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()  # 현재 ticks 값 받아오기

# 이벤트 루프
running = True  # 게임 진행 중 = True
while running:
    delta = clock.tick(30)  # FPS

######################################################################################################

    # 2. 이벤트 처리 : 키보드, 마우스 등

    for event in pygame.event.get():  # 이벤트 발생 목록
        if event.type == pygame.QUIT:  # X 박스를 클릭하는 이벤트 (종료 이벤트)
            running = False  # 게임 종료

        if event.type == pygame.KEYDOWN:  # 키를 누르는 이벤트
            if event.key == pygame.K_LEFT:  # 플레이어 좌 이동
                player_speed
            elif event.key == pygame.K_RIGHT:  # 플레이어 우 이동
                to_x += player_speed
            elif event.key == pygame.K_UP:  # 플레이어 상 이동
                to_y -= player_speed
            elif event.key == pygame.K_DOWN:  # 플레이어 하 이동
                to_y += player_speed

        if event.type == pygame.KEYUP:  # 키를 누르지 않으면 플레이어 이동 중지
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0  # 멈춤
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0  # 멈춤

######################################################################################################

    # 3. 플레이어 위치 정의

    player_x_position += to_x * delta
    player_y_position += to_y * delta

    # 가로 경계값 처리
    if player_x_position < 0:
        player_x_position = 0
    elif player_x_position > screen_width - player_width:
        player_x_position = screen_width - player_width

    # 세로 경계값 처리
    if player_y_position < 0:
        player_y_position = 0
    elif player_y_position > screen_height - player_height:
        player_y_position = screen_height - player_height

######################################################################################################

    # 4. 이미지 간의 충돌 처리

    # 충돌 처리를 위한 rect 정보 업데이트
    # 플레이어 rect
    player_rect = player.get_rect()
    player_rect.left = player_x_position
    player_rect.top = player_y_position
    # 장애물 rect
    obstacle_rect = obstacle.get_rect()
    obstacle_rect.left = obstacle_x_position
    obstacle_rect.top = obstacle_y_position

    # 충돌 처리 -> 충돌 시 게임 종료
    if player_rect.colliderect(obstacle_rect):
        running = False

######################################################################################################

    # 5. 게임 시간 설정

    # 타이머
    # 경과 시간 계산
    elapsed_time \
        = (pygame.time.get_ticks() - start_ticks) / 1000  # (현재 시간 - 시작 시간) / 1000(초)
    timer \
        = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))  # 출력 값, True, 색상
    # 시간 종료
    if total_time - elapsed_time <= 0:
        print("Time Out!!!")
        running = False

######################################################################################################

    # 6. 화면에 그리기

    # 구성 요소 그리기
    screen.blit(background, (0, 0))  # 배경 화면 그리기 (배경 화면 변수명, 좌표)
    screen.blit(player,
                (player_x_position, player_y_position))  # 플레이어 그리기 (플레이어 변수명, (플레이어 x좌표, y좌표))
    screen.blit(obstacle,
                (obstacle_x_position, obstacle_y_position))  # 장애물 그리기  장애물 변수명,  장애물 x좌표, y좌표))
    screen.blit(timer, (425, 10))  # 타이머 그리기 (타이머 변수명, (x좌표, y좌표))

    pygame.display.update()  # Redraw game screen - ESSENTIAL!!

######################################################################################################

# 시간 초과시 잠시 대기 (1.5초)
pygame.time.delay(1500)

# 게임 종료 - 필수
pygame.quit()
