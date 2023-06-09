import pygame

t = pygame.display.set_mode([1000, 700])

pygame.init()
m = pygame.font.SysFont("arial", 220, True, True)
mm = m.render("СЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ", True, [200, 200, 200])

m2 = pygame.font.SysFont("arial", 60, True, True)
mm2 = m2.render("Здраствуйте", True, [200, 200, 200])

lt = m2.get_height()
l = pygame.image.load("leave.png")
t.blit(l,[0,lt])

m3 = mm.get_height()

tm2 = mm2.get_width()
tm = t.get_width()-tm2

t.blit(mm,[0,0])
t.blit(mm2,[tm,m3])


while True:
    pygame.display.flip()
