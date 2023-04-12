import pygame
import random
import player as p
import ground as g
import breakk as b
import slot as s
import stone as st
import utils as ut
import mixer as mx
import time
WIDTH = 800
HEIGHT = 650
FPS = 30
cursor = pygame.image.load("res/bone.png")
cursor = pygame.transform.scale(cursor,(64,64))
# Задаем цвета 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

nick = input("Enter nickname: ")
print("You logged in as", nick)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("Leftover last, by Remote.NET Technologies")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
obj = pygame.sprite.Group()
slots = pygame.sprite.Group()
breakable = pygame.sprite.Group()
breaked = pygame.sprite.Group()
plyr = pygame.sprite.Group()
obj.add(p.Wall((WIDTH // 2 - 100, HEIGHT // 2), pygame.Surface((200, 50)), RED))
gr_x = 0
    
player = p.Player((WIDTH / 2, HEIGHT-200), pygame.Surface((30, 25)), pygame.Surface((30, 25)), RED, obj, screen)
plyr.add(player)
for i in range(20): 
    grd = g.Ground((gr_x, HEIGHT),player)
    obj.add(grd)
    breakable.add(grd)
    gr_x+=grd.rect.width-1

for x in range(20): 
    for y in range(9):
        grd = st.Stone((x*(st.grass_texture.get_width()-1),(HEIGHT+grd.rect.height-1)+y*(st.grass_texture.get_height()-1)),player)
        obj.add(grd)
        breakable.add(grd)      

for i in range(9):
    slots.add(s.Slot((50+(i*80),HEIGHT-40),i,player))

# slots.add(s.Slot((WIDTH/3+50,HEIGHT),1,player))
running = True
pygame.mouse.set_visible(False)
pointerImg_rect = cursor.get_rect()
now_fps = 0
timer = 0
fp = 0
loooped = 0
average = 0
font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
fps_text_avg = font.render("AVERAGE  FPS: " + str(round(clock.get_fps(),2)), True, BLUE)
fps_text = font.render("FPS: " + str(round(clock.get_fps(),2)), True, GREEN)
# create a rectangular object for the
# text surface object
textRect = fps_text.get_rect()
textAvgRect = fps_text_avg.get_rect()
# set the center of the rectangular object.
textRect.topleft = (0, 0)
textAvgRect.topleft = (0, 30)
while running:
    clock.tick(FPS)
    ytime = time.time()
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            WIDTH = event.w
            HEIGHT = event.h
            surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
            gr_x = 0
            player.rect.x = WIDTH / 2
            player.rect.y = 50
            obj = pygame.sprite.Group()
            breakable = pygame.sprite.Group()
            for i in range(20): 
                grd = g.Ground((gr_x, HEIGHT),player)
                obj.add(grd)
                breakable.add(grd)
                gr_x+=grd.rect.width-1

            for x in range(20): 
                for y in range(9):
                    grd = st.Stone((x*(st.grass_texture.get_width()-1),(HEIGHT+grd.rect.height-1)+y*(st.grass_texture.get_height()-1)),player)
                    obj.add(grd)
                    breakable.add(grd)      
            player.unt = obj
            player.x_vel=0
            player.y_vel=0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button
            # get the position of the mouse cursor
                
            # check for collisions between the mouse cursor and the grass sprite
                for sprite in breakable.sprites():
            
                    collide = sprite.rect.collidepoint(mouse_pos)
                    if collide and not player.is_breaking and (ut.calc_dist(player.rect.x, player.rect.y,sprite.rect.x, sprite.rect.y)/48)<3:
                        breaking = b.Break(sprite.rect.topleft,sprite,player,breaked)
                        all_sprites.add(breaking)
                        xd = mouse_pos[0]-player.rect.x
                        if xd<0 and player.left == False:
                            player.t()
                            player.left=True
                        elif xd > 0 and player.left == True:
                            player.t()
                            player.left= False
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
    x = player.x_vel
    y = player.y_vel
    for sp in obj.sprites():    
        a = sp.update(plauer=player,x_vel=x,y_vel=y)
    for sp in breaked.sprites():    
        a = sp.update(plauer=player,x_vel=x,y_vel=y)
        if ut.calc_dist(player.rect.centerx,player.rect.centery,sp.rect.centerx, sp.rect.centery)/48 < 1:
            player.add_inv(sp.daughter(1))
            mx.play(mx.pickup)
            sp.kill()
    screen.fill(BLACK)
    
    obj.draw(screen)
    
    all_sprites.draw(screen)
    slots.update(scr=screen)
    
    breaked.draw(screen)
    plyr.draw(screen)
    plyr.update()
    slots.draw(screen)
    pointerImg_rect.center  = pygame.mouse.get_pos()
    if ut.checkFocus(mouse_pos, screen):
        screen.blit(cursor, pointerImg_rect)
    screen.blit(fps_text, textRect)
    screen.blit(fps_text_avg, textAvgRect)
    pygame.display.flip()  
    now_fps+=1
    timer+= time.time()-ytime
    average+= clock.get_fps()
    loooped += 1
    fps_text_avg = font.render("AVERAGE FPS: " + str(round(average/loooped,2)), True, BLUE)
    fps_text = font.render("FPS: " + str(round(clock.get_fps(),2)), True, GREEN)
pygame.quit()