import pygame, sys
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (50, 50, 20, 20))  # Green square
    pygame.display.flip()
    clock.tick(60)