import random
import pygame

t = pygame.display.set_mode([1000, 700])

pygame.init()
m = pygame.font.SysFont("arial", 220, True, True)
mm = m.render("СЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ", True, [200, 200, 200],[0,255,0])

m2 = pygame.font.SysFont("arial", 60, True, True)
mm2 = m2.render("Здраствуйте", True, [200, 200, 200],[0,0,255])

m3 = pygame.font.SysFont("arial", random.randint(20,80),True, True )
mm3 = m3.render("Ежики", True, [100,200,78],[255,0,0])

tm2 = mm2.get_width()
tm = t.get_width()-tm2
m20 = mm.get_height()
t.blit(mm,[0,0])
t.blit(mm2,[tm,m20])

lt = mm.get_height()
lt2 = mm2.get_height()
l = pygame.image.load("leave.png")
t.blit(l, [0, lt+lt2])

tl = l.get_height()
tl2 = mm2.get_height()
tl3 = mm.get_height()
u = pygame.image.load("ulibka.png")
t.blit(u, [900, tl2+tl+tl3])

tl4 = u.get_height()
t.blit(mm3, [0,tl+lt2+tl3+tl4])

while True:
    pygame.display.flip()
