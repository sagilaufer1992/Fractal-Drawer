import pygame
from fractals.sierpinski_triangle import sierpinski_triangle
from fractals.koch_snowflake import koch_triangle

pygame.init()

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fractal Painter')

white = (255, 255, 255)
black = (0, 0, 0)

game_display.fill(white)

# sierpinski_triangle(game_display, (100, 500), 500, black, white, 4)
koch_triangle(game_display, black, (100, 400), 360, 4)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()
