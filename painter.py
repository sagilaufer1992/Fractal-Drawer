import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Fractal Painter')

white = (255,255,255)
black = (0,0,0)

gameDisplay.fill(white)

pygame.draw.line(gameDisplay, black, (100,200), (100,600),1)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()



