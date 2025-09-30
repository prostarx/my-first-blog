#class Cat:
#    c = ("John")
#    print(c.meow(3))
#    def __init__(self, name ="Кот"):
#        self.name = name
#
#    def meow(self, times=1):
#
#        try:
#            n = int(times)
#        except Exception:
#            n = 1
#            if n < 1:
#                n = 1
#                return " ".join("Мяу") * n)

import pygame
pygame.init()
dis=pygame.display.set_mode((500,400))

dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()
    r = pygame.Rect(150, 100, 200, 200)
    b = pygame.Rect(175, 200, 150, 100)
    c = pygame.Rect(250, 120, 50, 50)
    color = 255,0,0
    pygame.draw.rect(dis,color,r, 0)
    color1 = 100, 100, 100
    pygame. draw.rect(dis, color1, b, 0)
    color2 = 123, 100, 212
    pygame.draw.rect(dis, color2, c, 0)
    color3 = 138, 43, 226
    color4 = 155, 30, 204
    color5 = 255, 228, 225

    pygame.draw.line(dis,color3, [250, 10], [150, 100], width=10)
    pygame.draw.line(dis,color3, [250, 10], [349, 100], width=10)
    pygame.display.update()



quit()