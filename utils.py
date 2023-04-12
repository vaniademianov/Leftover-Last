import pygame
def calc_dist(x1,y1,x2,y2):
   return pygame.math.Vector2(x1, y1).distance_to((x2, y2))