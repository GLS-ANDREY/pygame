# Ocnovi

import pygame

a = pygame.Surface([1000,1000])

pygame.draw.line(a,[252,248,74],[0,0],[1000,1000],10)
pygame.draw.line(a,[252,248,74],[1000,0],[0,1000],10)
pygame.image.save(a,"aboba.png")

