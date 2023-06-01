import pygame
import random
import time

t = pygame.Surface([1000, 1000])

g = pygame.image.load("aboba.png")
g2 = pygame.transform.scale(g, [random.randint(100, 300), random.randint(100, 300)])
t.blit(g2, [0, 0])

p = pygame.image.load("popugai.png")
gg22 = g2.get_height()
t.blit(p,[3,gg22])

gg22 = g2.get_width()
h = pygame.image.load("stick.png")
t.blit(h, [gg22, 0])
pygame.image.save(t, "img.png")

# br = pygame.Rect(0, 0, 30, 30)z
# pygame.draw.rect(t, [230, 40, 155], br)
#
# g = pygame.image.load("aboba.png")
# t.blit(g, [200, 100])
# pygame.image.save(t, "br.jpg")
