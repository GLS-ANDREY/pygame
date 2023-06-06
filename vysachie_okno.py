import pygame

t = pygame.display.set_mode([1000, 700])
pygame.init()
m = pygame.font.SysFont("arial", 20, True, True)
mm = m.render("СЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫЫ", True, [200, 200, 200])
m2 = pygame.font.SysFont("arial", 30, True, True)
mm2 = m2.render("Здраствуйте, арабы мусульмане", True, [200, 200, 200])
m3 = mm.get_height()
t.blit(mm,[0,0])
t.blit(mm2,[0,m3])
while True:
    pygame.display.flip()
