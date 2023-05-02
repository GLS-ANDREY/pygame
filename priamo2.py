import pygame
import random
import time

t = pygame.display.set_mode([1000, 700])  # Обычный режим
# t = pygame.display.set_mode([0, 0],pygame.FULLSCREEN)# Полноэкранный режим
o = random.randint(0, 400)
f = random.randint(0, 400)
polet = pygame.Rect(100, 150, 300, 200)
c = random.randint(100,300)
goluboi = pygame.Rect(700, 0, c, 700)
right_g = goluboi.right
y_m = random.randint(0,660)
x_m = random.randint(0,1000)
monet = pygame.Rect(right_g-40,y_m, 40, 40)
polet.centerx = 500
polet.top = 0
s_y = 1
while True:
    print(polet)
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
    pygame.display.flip()
