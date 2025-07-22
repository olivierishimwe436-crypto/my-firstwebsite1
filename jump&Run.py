import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running and Jumping Race")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_width, player_height = 40, 60
player_x, player_y = 50, HEIGHT - player_height - 40
player_vel_x = 0
player_vel_y = 0
jumping = False
gravity = 0.8
jump_power = -15

# Finish line
finish_line_x = 700

# Ground
ground_y = HEIGHT - 40

# Game font
font = pygame.font.SysFont(None, 48)
winner_text = ""

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keypress handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_vel_x = 5
    elif keys[pygame.K_LEFT]:
        player_vel_x = -5
    else:
        player_vel_x = 0

    if not jumping and keys[pygame.K_SPACE]:
        jumping = True
        player_vel_y = jump_power

    # Update player position
    player_x += player_vel_x

    if jumping:
        player_y += player_vel_y
        player_vel_y += gravity

        if player_y >= HEIGHT - player_height - 40:
            player_y = HEIGHT - player_height - 40
            jumping = False

    # Check win condition
    if player_x + player_width >= finish_line_x:
        winner_text = "You Win!"

    # Draw ground
    pygame.draw.rect(screen, GREEN, (0, ground_y, WIDTH, 40))

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw finish line
    pygame.draw.line(screen, BLACK, (finish_line_x, 0), (finish_line_x, HEIGHT), 4)

    # Draw winner text
    if winner_text:
        text_surface = font.render(winner_text, True, (0, 0, 0))
        screen.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, 100))

    pygame.display.flip()
    clock.tick(FPS)
