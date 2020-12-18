import pygame
import sys
import random


def drawFloor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + 288, 450))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(400, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(400, random_pipe_pos - 150))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 450:
        return False

    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -movement * 3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_idx]
    new_bird_rect = new_bird.get_rect(center = (144, bird_rect.centery))

    return new_bird, new_bird_rect

def score_disp(game_active):
    if game_active:
        score_surface = game_font.render('Score: '+ str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (144, 50))
        screen.blit(score_surface, score_rect)
    else:
        score_surface = game_font.render('Score: '+ str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (144, 50))
        screen.blit(score_surface, score_rect)   
        
        hi_score_surface = game_font.render('High Score: '+ str(int(hi_score)), True, (255, 255, 255))
        hi_score_rect = score_surface.get_rect(center = (144, 25))
        screen.blit(hi_score_surface, hi_score_rect)




pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
game_font = pygame.font.Font('assets/04B_19.ttf',20)

# Game Variables
clk_rate = 60
gravity = 0.4
movement = 0
jump = gravity * clk_rate / 3
floor_x_pos = 0
game_on = True
score = 0
hi_score = 0


# Background Image
bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()

# Floor Image
floor_surface = pygame.image.load('assets/sprites/base.png').convert()

# Bird Image & its rectangle
bird_down = pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha()
bird_mid = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha()
bird_up = pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha()
bird_frames = [bird_down, bird_mid, bird_up]
bird_idx = 0
bird_surface = bird_frames[bird_idx]
bird_rect = bird_surface.get_rect(center=(144, 256))
# bird_surface = pygame.image.load(
#     'assets/sprites/bluebird-midflap.png').convert_alpha()
# bird_rect = bird_surface.get_rect(center=(144, 256))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


# Pipe Image
pipe_surface = pygame.image.load('assets/sprites/pipe-green.png').convert()
pipe_list = []


# Make Pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1000)
pipe_height = [225, 300, 400]

# Game over
game_over_surface = pygame.image.load('assets/sprites/gameover.png').convert()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_on:
                movement = 0
                movement -= jump
                # print("space pushed")
            if event.key == pygame.K_SPACE and game_on == False:
                game_on = True
                pipe_list.clear()
                bird_rect.center = (144, 256)
                movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            # print(pipe_list)
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_idx < 2:
                bird_idx += 1
            else:
                bird_idx = 0

            bird_surface, bird_rect = bird_animation()

    # Background
    screen.blit(bg_surface, (0, 0))

    if game_on:
        # Bird
        movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += movement
        screen.blit(rotated_bird, bird_rect)
        game_on = check_collision(pipe_list)

    # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

    # Score
        score_disp(game_on)
        score += 0.01
    else:
        screen.blit(game_over_surface, (50, 200))
    
    if score > hi_score:
        hi_score = score
    score_disp(game_on)
    # Floor
    floor_x_pos -= 1
    drawFloor()
    if floor_x_pos <= -288:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(clk_rate)
