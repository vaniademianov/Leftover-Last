import pygame
def calc_dist(x1,y1,x2,y2):
   return pygame.math.Vector2(x1, y1).distance_to((x2, y2))
def checkFocus(e, display):
   x, y = e
   MX, MY = display.get_size()
   MX -= 1 # 0 - based
   MY -= 1
   if x <= 0 or y <= 0 or x >= MX or y >= MY:
      return False
   else:
      return True