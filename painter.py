import pygame
from utils.polygon_drawings import equilateral_triangle

pygame.init()

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fractal Painter')

white = (255, 255, 255)
black = (0, 0, 0)

game_display.fill(white)

equilateral_triangle(game_display, black, (100, 500), 200, True)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()
