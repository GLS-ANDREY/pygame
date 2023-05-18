import pygame
import random
import time

t = pygame.display.set_mode([1000, 700])

polet = pygame.Rect(100, 150, 300, 200)
polet.centerx = 800
polet.top = 0

c = random.randint(100,300)
goluboi = pygame.Rect(700, 0, c, 700)
y_m = random.randint(0,660)
monet = pygame.Rect(0,y_m, 40, 40)
monet.x = random.randint(goluboi.left,goluboi.right-40)
mikro_monet = pygame.Rect(0,0,10,10)

s_y = 1
while True:
    print(polet)
    mikro_monet.y = random.randint(monet.top,monet.bottom-10)
    mikro_monet.x = random.randint(monet.left,monet.right-10)
    if polet.x == 1000:
        polet.right = 0
    polet.x = polet.x + 1
    polet.y = polet.y + s_y
    if polet.bottom == 700:
        s_y = -1
    if polet.top == 0:
        s_y = 1
    # ------------------------------------------------
    t.fill([0, 0, 0])

    pygame.draw.rect(t, [100, 200, 255], goluboi)
    pygame.draw.rect(t, [40, 50, 60], polet)
    pygame.draw.rect(t, [255,241,41], monet)
    pygame.draw.rect(t,[255,121,9],mikro_monet)
    pygame.display.flip()