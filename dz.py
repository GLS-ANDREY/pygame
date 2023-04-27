#Первое дз
# import pygame
# import random
# import time
#
# t = pygame.display.set_mode([1000, 700])
#
# while True:
#     t.fill([0, 0, 0])
#     b = random.randint(0, 750)
#     r = random.randint(0, 750)
#     u = random.randint(0, 200)
#     v = random.randint(0, 255)
#     g = random.randint(0, 255)
#     m = random.randint(0, 255)
#     pygame.draw.circle(t, [g, m, v], [300,300],u)
#     # time.sleep(0.3)
#     pygame.display.flip()



#Второе дз

# import pygame
#
# n = pygame.display.set_mode([1000, 700])  # Обычный режим
# # t = pygame.display.set_mode([0, 0],pygame.FULLSCREEN)# Полноэкранный режим
# r = pygame.Rect(200,250,200,250)
# r.right = 1000
# l = pygame.Rect(200,250,200,250)
# l.left = 0
# t = pygame.Rect(400,250,200,250)
# t.top = 0
# b = pygame.Rect(400,250,200,250)
# b.bottom = 700
# while True:
#     pygame.draw.rect(n, [40, 50, 60], r)
#     pygame.draw.rect(n, [40, 50, 60], l)
#     pygame.draw.rect(n, [40, 50, 60], t)
#     pygame.draw.rect(n, [40, 50, 60], b)
#     pygame.display.flip()