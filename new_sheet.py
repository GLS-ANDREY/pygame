import random
import pygame

t = pygame.display.set_mode([1000, 700])

p = pygame.image.load("popugai.png")

tr = pygame.transform.scale(p,[random.randint(20,200),random.randint(20,200)])
gw = tr.get_width()
gh = tr.get_height()
t.blit(tr,[100,100])
t.blit(tr,[gh,gw])



while True:
    pygame.display.flip()
