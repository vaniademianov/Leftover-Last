import pygame
import random
import player as p
import ground as g
WIDTH = 800
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)





pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Leftover last, by RemoteAccess01 <3")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
obj = pygame.sprite.Group()
obj.add(p.Wall((WIDTH // 2 - 100, HEIGHT // 2), pygame.Surface((200, 50)), RED))
obj.add(g.Ground((0, HEIGHT), 64))
player = p.Player((WIDTH / 2, HEIGHT-200), pygame.Surface((30, 25)), pygame.Surface((30, 25)), RED, obj)
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            WIDTH = event.w
            HEIGHT = event.h
            surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)

            player.rect.x = WIDTH / 2
            player.rect.y = 50
    all_sprites.update()
    obj.update(plauer=player)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    obj.draw(screen)
    pygame.display.flip() 

pygame.quit()