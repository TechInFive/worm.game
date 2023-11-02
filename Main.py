import pygame

from Bean import Bean
from Worm import Worm

from constants import BACKGROUND, WORM, BEAN, WIDTH, HEIGHT, BLOCK_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE))
pygame.display.set_caption("Worm Game")

def draw_block(position, color):
    pygame.draw.rect(screen, color, (position[0]*BLOCK_SIZE, position[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_bean(bean):
    draw_block(bean.position, BEAN)

def draw_worm(worm):
    for segment in worm.body:
        draw_block(segment, WORM)

worm = Worm()
beans = [Bean() for _ in range(10)]

running = True
while running:
    screen.fill(BACKGROUND)

    for bean in beans:
        draw_bean(bean)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                worm.left()
            elif event.key == pygame.K_RIGHT:
                worm.right()
            elif event.key == pygame.K_UP:
                worm.up()
            elif event.key == pygame.K_DOWN:
                worm.down()

    worm.move()

    draw_worm(worm)

    head = worm.head()
    if head in worm.body[1:] or \
       head[0] < 0 or head[1] < 0 or \
       head[0] > WIDTH - 1 or head[1] > HEIGHT - 1:
        running = False

    for i in range(len(beans)):
        if worm.head() == beans[i].position:
            worm.grow()
            beans[i] = Bean()
            break

    pygame.display.flip()
    pygame.time.Clock().tick(10)

pygame.quit()