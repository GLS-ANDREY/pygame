import pygame
import random
import time

t = pygame.display.set_mode([1000, 700])  # Обычный режим
# t = pygame.display.set_mode([0, 0],pygame.FULLSCREEN)# Полноэкранный режим
o = random.randint(0, 400)
f = random.randint(0, 400)
r = pygame.Rect(100, 150, 300, 200)
c = random.randint(100,300)
r2 = pygame.Rect(700, 0, c, 700)
r3 = pygame.Rect(500,700,40,40)

r.centerx = 500
r.top = 0
s_y = 1
while True:
    print(r)
    if r.x == 1000:
        r.right = 0
    r.x = r.x + 1
    r.y = r.y + s_y
    if r.bottom == 700:
        s_y = -1
    if r.top == 0:
        s_y = 1
    # ------------------------------------------------
    t.fill([0, 0, 0])
    pygame.draw.rect(t, [100, 200, 255], r2)
    pygame.draw.rect(t, [40, 50, 60], r)
    pygame.draw.rect(t,[255,241,41],r3)
    pygame.display.flip()
