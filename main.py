import pygame
import random
import player as p
import ground as g
import breakk as b
import slot as s
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
slots = pygame.sprite.Group()
breakable = pygame.sprite.Group()
obj.add(p.Wall((WIDTH // 2 - 100, HEIGHT // 2), pygame.Surface((200, 50)), RED))
gr_x = 0
for i in range(64): 
    grd = g.Ground((gr_x, HEIGHT))
    obj.add(grd)
    breakable.add(grd)
    gr_x+=grd.rect.width-1
    
player = p.Player((WIDTH / 2, HEIGHT-200), pygame.Surface((30, 25)), pygame.Surface((30, 25)), RED, obj)
all_sprites.add(player)
slots.add(s.Slot((WIDTH/3,HEIGHT),0,player))
# slots.add(s.Slot((WIDTH/3+50,HEIGHT),1,player))
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button
            # get the position of the mouse cursor
                mouse_pos = pygame.mouse.get_pos()
            # check for collisions between the mouse cursor and the grass sprite
                for sprite in breakable.sprites():
                    collide = sprite.rect.collidepoint(mouse_pos)
                    if collide and not player.is_breaking:
                        breaking = b.Break(sprite.rect.topleft,sprite,player)
                        all_sprites.add(breaking)
                        break
    all_sprites.update()
    
    obj.update(plauer=player)
    screen.fill(BLACK)
    
    obj.draw(screen)
    all_sprites.draw(screen)
    slots.update(scr=screen)
    slots.draw(screen)
    
    pygame.display.flip() 

pygame.quit()