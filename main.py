import pygame
import random
import player as p
import ground as g
import breakk as b
import slot as s
import stone as st
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
for x in range(64): 
    for y in range(9):
        HEIGHT+48
        grd = st.Stone((x*46,(HEIGHT+46)+y*46))
        obj.add(grd)
        breakable.add(grd)
    
player = p.Player((WIDTH / 2, HEIGHT-200), pygame.Surface((30, 25)), pygame.Surface((30, 25)), RED, obj)
all_sprites.add(player)
for i in range(9):
    slots.add(s.Slot((50+(i*80),HEIGHT-40),i,player))
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
        if event.type == pygame.MOUSEWHEEL:
            x = event.y
            if x>0:
                player.slot += 1
            else:
                player.slot -= 1

            if player.slot > 8:
                player.slot = 0
            if player.slot < 0:
                player.slot = 8    
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_1]:
                player.slot = 0
            if pressed[pygame.K_2]:
                player.slot = 1
            if pressed[pygame.K_3]:
                player.slot = 2
            if pressed[pygame.K_4]:
                player.slot = 3
            if pressed[pygame.K_5]:
                player.slot = 4
            if pressed[pygame.K_6]:
                player.slot = 5
            if pressed[pygame.K_7]:
                player.slot = 6
            if pressed[pygame.K_8]:
                player.slot = 7
            if pressed[pygame.K_9]:
                player.slot = 8

    all_sprites.update()
    
    obj.update(plauer=player)
    screen.fill(BLACK)
    
    obj.draw(screen)
    all_sprites.draw(screen)
    slots.update(scr=screen)
    slots.draw(screen)
    
    pygame.display.flip()  

pygame.quit()