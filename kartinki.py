import pygame
import random
import time

t = pygame.Surface([1000, 1000])

br = pygame.Rect(0, 0, 30, 30)
pygame.draw.rect(t, [230, 40, 155], br)

g = pygame.image.load("aboba.png")
pygame.image.save(t, "br.jpg")
t.blit(g, [200, 100])
pygame.image.save(t, "br.jpg")
