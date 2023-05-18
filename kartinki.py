import pygame
import random
import time


t = pygame.Surface([1000,1000])


niger = pygame.Rect(0,0,30,30)
pygame.draw.rect(t,[0,0,20],niger)

pygame.image.save(t, "niger.jpg")

