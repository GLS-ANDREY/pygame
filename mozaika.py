import os
import random
import pygame

t = pygame.display.set_mode([1000, 700])

p = pygame.image.load("popugai.png")
u = pygame.image.load("ulibka.png")
st = pygame.image.load("stick.png")
s = [u,p,st]

b = 0
for a in range(10):
    mr = random.choice(s)
    tr = pygame.transform.scale(mr,[random.randint(20,120),random.randint(20,120)])
    sv = tr.get_height()
    t.blit(tr, [0, b])
    b = b + sv


while True:
    pygame.display.flip()
