import random
import pygame

t = pygame.display.set_mode([1000, 700])

p = pygame.image.load("popugai.png")
u = pygame.image.load("ulibka.png")

tr = pygame.transform.scale(p,[random.randint(150,300),random.randint(150,300)])
gh = tr.get_height()
gw = tr.get_width()
tu = pygame.transform.scale(u,[gw/2,gh/2])
t.blit(tr,[100,100])
t.blit(tr,[gw+100,100])
t.blit(tr,[100,gh+100])
t.blit(tu,[100+gw,100+gh])
pygame.draw.rect(t,[200, 200, 200],[gw+100,gh+100,gw,gh],5)
pygame.draw.rect(t,[201, 201, 201],[100,100,gw+gw,gh+gh],5)


while True:
    pygame.display.flip()
