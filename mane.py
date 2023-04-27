# Ocnovi

import pygame

a = pygame.Surface([1000,1000])

a.fill([252,248,74])

pygame.draw.line(a,[252,248,74],[0,0],[1000,1000],10)
pygame.draw.line(a,[252,248,74],[1000,0],[0,1000],10)
# pygame.draw.circle(a,[195,15,31],[500,170],150)
pygame.draw.rect(a,[195,15,31],[380,700,250,250],150)
pygame.draw.circle(a,[0,0,0],[200,550],120)
pygame.draw.circle(a,[0,0,0],[800,550],120)
pygame.draw.rect(a,[0,0,0],[50,300,300,100])
pygame.draw.rect(a,[0,0,0],[650,300,300,100])

pygame.image.save(a,"aboba.png")

g = pygame.image.load("img.png")

pygame.draw.circle(g,[195,15,31],[250,250],70)
pygame.image.save(g,"imge.png")


