import pygame
import sys


def drawFloor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + 288, 450))


pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()

# Game Variables
clk_rate = 60
gravity = 0.2
movement = 0
jump = gravity * clk_rate / 1.8


# Background Image
bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()

# Floor Image
floor_surface = pygame.image.load('assets/sprites/base.png').convert()

# Bird Image & its rectangle
bird_surface = pygame.image.load('assets/sprites/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (144, 256))



floor_x_pos = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                movement = 0
                movement -= jump
                print("space pushed")

    # Background
    screen.blit(bg_surface, (0, 0))

    # Bird
    movement += gravity
    bird_rect.centery += movement
    screen.blit(bird_surface, bird_rect)

    # Floor
    floor_x_pos -= 1
    drawFloor()
    if floor_x_pos < -288:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(clk_rate)
    
