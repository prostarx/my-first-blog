import pygame
import random

pygame.init()
dis=pygame.display.set_mode((1000, 750))
dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()
    color1 = 255, 255, 255
    color2 = 0, 0, 0
    color3 = 210, 105, 30
    pygame.draw.circle(dis,color1,[500, 200], 75, 0)
    pygame.draw.circle(dis,color2,[470, 180], 7, 0)
    pygame.draw.circle(dis,color2,[530, 180], 7, 0)
    pygame.draw.circle(dis,color1,[500, 325], 100, 0)
    pygame.draw.circle(dis,color1,[500, 450], 120, 0)
    pygame.draw.polygon(dis,(210, 105, 30),[(500, 190), (500, 210), (560,200)])
    pygame.display.update()
