import os
import random
import pygame

t = pygame.display.set_mode([1000, 700])

p = pygame.image.load("popugai.png")
b = 0
for a in range(5):
    t.blit(p, [0, b])
    b = b + 50

while True:
    pygame.display.flip()
