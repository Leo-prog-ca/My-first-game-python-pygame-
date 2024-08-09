import pygame
import random

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
OBSTACLE_SPEED = 5
PLAYER_SPEED = 10

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Avoid the Obstacles")

player_x = WINDOW_WIDTH // 2 - PLAYER_SIZE // 2
player_y = WINDOW_HEIGHT - 2 * PLAYER_SIZE

obstacles = []
for _ in range(5):
    x = random.randint(0, WINDOW_WIDTH - OBSTACLE_SIZE)
    y = random.randint(-WINDOW_HEIGHT, -OBSTACLE_SIZE)
    obstacles.append([x, y])

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED

    for obs in obstacles:
        obs[1] += OBSTACLE_SPEED
        if obs[1] > WINDOW_HEIGHT:
            obs[1] = random.randint(-OBSTACLE_SIZE, -OBSTACLE_SIZE)
            obs[0] = random.randint(0, WINDOW_WIDTH - OBSTACLE_SIZE)


    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    for obs in obstacles:
        obstacle_rect = pygame.Rect(obs[0], obs[1], OBSTACLE_SIZE, OBSTACLE_SIZE)
        if player_rect.colliderect(obstacle_rect):
            running = False


    window.fill(BACKGROUND_COLOR)
    pygame.draw.rect(window, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    for obs in obstacles:
        pygame.draw.rect(window, OBSTACLE_COLOR, (obs[0], obs[1], OBSTACLE_SIZE, OBSTACLE_SIZE))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
