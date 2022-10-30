import pygame
from pygame.draw import *
from pygame.color import THECOLORS

pygame.init()


FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill(THECOLORS['orange'])

circle(screen, (255, 255, 153), (200, 200), 150)
circle(screen, (0, 0, 0), (125, 170), 30, 5)
circle(screen, (0, 0, 0), (275, 170), 25, 5)
circle(screen, (255, 0, 0), (125, 170), 30)
circle(screen, (255, 0, 0), (275, 170), 25)
circle(screen, (0, 0, 0), (125, 170), 15)
circle(screen, (0, 0, 0), (275, 170), 15)
line(screen, (0, 0, 0), [165, 145], [50, 100], 20)
line(screen, (0, 0, 0), [245, 145], [350, 100], 20)
rect(screen, (0, 0, 0), (145, 255, 120, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
