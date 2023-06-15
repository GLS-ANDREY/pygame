import os
import random
import pygame

t = pygame.display.set_mode([1000, 700])

s = ["Это его папа", "ulibka.png", "Это его брат", "popugai.png"]
s2 = random.choice(s)
s3 = os.path.exists(s2)

if s3 == True:
    u = pygame.image.load(s2)
    t.blit(u, [0, 0])

if s3 == False:
    pygame.init()
    b = pygame.font.SysFont("arial", 80, True, True)
    bb = b.render(s2, True, [200, 200, 200], [0, 255, 0])
    t.blit(bb, [0, 0])

while True:
    pygame.display.flip()
