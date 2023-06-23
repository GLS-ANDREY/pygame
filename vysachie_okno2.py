import os
import random
import pygame

t = pygame.display.set_mode([1000, 700])

s = ["Это его папа", "ulibka.png", "Это его брат", "popugai.png"]

for a in s:
    s3 = os.path.exists(a)
    if s3 == False:
        pygame.init()
        b = pygame.font.SysFont("arial", 80, True, True)
        bb = b.render(a, True, [200, 200, 200], [0, 255, 0])
        t.blit(bb, [0, random.randint(0, 600)])

    if s3 == True:
        u = pygame.image.load(a)
        t.blit(u, [0, random.randint(0, 600)])

while True:
    pygame.display.flip()
