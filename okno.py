import pygame
import random

# t = pygame.display.set_mode([1000, 700])#Обычный режим
t = pygame.display.set_mode([0, 0],pygame.FULLSCREEN)# Полноэкранный режим

while True:
    g = random.randint(0, 255)
    h = random.randint(0, 255)
    m = random.randint(0, 255)
    t.fill([g, h, m])#один овал
    b = random.randint(0, 750)
    v = random.randint(0, 750)
    r = random.randint(0, 750)
    u = random.randint(0, 750)
    g = random.randint(0, 255)
    h = random.randint(0, 255)
    m = random.randint(0, 255)
    pygame.draw.ellipse(t, [h, m, g], [r, u, b, v])
    pygame.display.flip()
