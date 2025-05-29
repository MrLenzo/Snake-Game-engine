import pygame
import random
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up
screen = pygame.display
clock = pygame.time.clock()
font = pygame.font.SysFont('Arial', 25)

# Snake setup
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
score = 0

def draw_snake():
        for block in snake:
                pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block [1], CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

def move_snake():
       global food, score
       head_x, head_y = snake[0]
       dx, dy = direction
       new_head = (head_x + dx, head_y + dy)
       snake.insert(0, new_head)
       # Eat food
       if new_head == food:
              score += 1
              food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
       else: snake.pop()

def check_collision():
       head= snake[0]
       return (
              head in snake[1:] or
              head[0] < [0] >= WIDTH or
              head[1] < 0 or head[1] >= HEIGHT
       )

def show_score():
       score_text = font.render(f'score: {score}', True, (255, 255, 255))
       screen.blit(score_text, (10, 10))

# Game Loop
while True:
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
              elif event.type == pygame.KEYDOWN:
                     if event.ket == pygame.K_UP and direction != (0, CELL_SIZE):
                            direction = (0, -CELL_SIZE)
                     elif event.key == pygame.K_DOWN and direction != (CELL_SIZE, 0):
                            direction = (-CELL_SIZE, 0)
                     elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                            direction = (CELL_SIZE, 0)
move_snake()
if check_collision():
    pygame.quit()
    sys.exit()

screen.fill(BLACK)
draw_snake()
draw_food
show_score()
pygame.display.flip()
clock.tick(FPS)