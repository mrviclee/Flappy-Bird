import pygame
import sys


def drawFloor():
    screen.blit(floor_surface, (floor_x_pos, 400))
    screen.blit(floor_surface, (floor_x_pos + 288, 400))


pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()

# Background Image
bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()

# Background Image
floor_surface = pygame.image.load('assets/sprites/base.png').convert()

floor_x_pos = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    floor_x_pos -= 1
    drawFloor()
    if floor_x_pos < -288:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(20)
    
