import pygame
import random

t = pygame.display.set_mode([1000, 700])  # Обычный режим
# t = pygame.display.set_mode([0, 0],pygame.FULLSCREEN)# Полноэкранный режим

u = 0
r = 0
b = 0
m = 0
o = 0
while True:
    u = u + 0.01
    if u >= 255:
        u = 0
    if b >= 255:
        b = 0
    if r >= 255:
        r = 0
    print([u,r,b])
    m = m + 0.01
    o = o + 0.01
    r = r + 0.02
    b = b + 0.03
    pygame.draw.rect(t, [u, r, b], [m, o, m, o])
    pygame.display.flip()