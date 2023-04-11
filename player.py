import pygame
WIDTH = 800
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

blue_img = pygame.image.load("res/blue.png")
blue_resized = pygame.transform.scale(blue_img, (blue_img.get_width()/5,blue_img.get_height()/5))
hit_img = pygame.image.load("res/hitbox.png")
hit_resized = pygame.transform.scale(hit_img, (hit_img.get_width()/9,hit_img.get_height()/7))
class Part(pygame.sprite.Sprite):
    def __init__(self, parent, pos,unt):
        self.image = hit_resized
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.player = parent
        self.unt = unt
    def update(self) -> None:
        self.rect.center = self.player.rect.center

    def left_check(self) -> bool:
        self.rect.x -= 5
        if pygame.sprite.spritecollide(self, self.unt, False):
            self.rect.x += 5
            return False
        else:
            self.rect.x += 5
            return True
    def right_check(self) -> bool:
        self.rect.x += 5
        if pygame.sprite.spritecollide(self, self.unt, False):
            self.rect.x -= 5
            return False
        else:
            self.rect.x -= 5
            return True
    def up_check(self) -> bool:
        self.rect.y -= 10
        if pygame.sprite.spritecollide(self, self.unt, False):
            self.rect.y += 10
            return False
        else:
            self.rect.y += 10
            return True
    def down_check(self) -> bool:
        self.rect.y += 14
        if pygame.sprite.spritecollide(self, self.unt, False):
            self.rect.y -= 14
            return False
        else:
            self.rect.y -= 14
            return True
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface1, surface2, color, unt):
        pygame.sprite.Sprite.__init__(self)
        x, y = pos
        self.image = blue_resized
        self.rect = self.image.get_rect()
        self.hitbox = Part(self,pos,unt)
        self.rect.topleft = pos
        self.speed = 1.5
        self.max_speed = 10
        self.min_speed = -10
        self.is_jump = True
        self.x_vel = 0
        self.y_vel = 0
        self.unt = unt
        self.left=False
        self.is_breaking = True
        self.inv = [None, None, None,None,None,None,None,None,None,None]
        self.slot = 0
        self.walls_updated = 0
    def update(self):
        
        keys = pygame.key.get_pressed()
        self.hitbox.update()
        dh = self.hitbox.down_check()
        if keys[pygame.K_s]:
            self.y_vel = 10
            
        if keys[pygame.K_w] and not self.is_jump and not dh:
            self.y_vel = -12
            self.is_jump = True
        if keys[pygame.K_d]:
            if self.x_vel < self.max_speed: self.x_vel+= self.speed

        elif keys[pygame.K_a]:
            if self.x_vel > self.min_speed: self.x_vel+= -self.speed
        if self.is_jump and self.y_vel > 11:
            self.y_vel = 0
            self.is_jump = False
        
        uh =self.hitbox.up_check()
        rc = self.hitbox.right_check()
        lc =self.hitbox.left_check()
        if self.y_vel > 0 and not dh:
            self.y_vel = 0
            self.is_jump = False
        if self.y_vel < 0 and not uh:
            self.y_vel = 0
            self.is_jump = False
        if self.x_vel > 0 and not rc:
            self.x_vel = 0
        if self.x_vel < 0 and not lc:
            self.x_vel = 0
        self.x_vel *= 0.75
        if dh:
            self.y_vel += 1
            self.is_breaking=False
        if self.x_vel > 0 and self.x_vel<0.2:
            self.x_vel = 0
        if self.x_vel < 0 and self.x_vel> -0.2:
            self.x_vel = 0
        if self.x_vel != 0:
            self.is_breaking = False
        if self.x_vel<0 and self.left == False:
            self.image=pygame.transform.flip(self.image,True,False)
            self.left=True
        elif self.x_vel > 0 and self.left == True:
            self.image=pygame.transform.flip(self.image,True,False)
            self.left= False
    def add_inv(self, item):
        d = False
        for o in self.inv:
            if o != None:
                if o.count < 64 and o.type == item.type and not d:
                    if o.count +item.count <= 64:
                        o.count = o.count + item.count
                        d = True
                        break
                    else:
                        o.count = 64
                        ik = (o.count +item.count) -64
                        nw = item
                        nw.count = ik
                        self.inv.append(ik)
                        d = True
                        break
        if not d:
            for i in range(len(self.inv)):
                if self.inv[i] == None:
                    self.inv[i] = item
                    return
            self.inv.append(item)       
            
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, surface, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = surface
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def update(self, plauer,x_vel,y_vel):
        a = self.rect.center
        self.rect.centerx += -x_vel
        self.rect.centery += -y_vel
# class Part(pygame.sprite.Sprite):
#     def __init__(self, pos, surface):
#         self.image = surface
#         self.rect = self.image.get_rect()
#         # self.rect.center = pos
#         self.rect.topleft = pos
# walls_v_left = pygame.sprite.Group()
# walls_v_right = pygame.sprite.Group()
# walls_h = pygame.sprite.Group()
# # walls_h.add(Wall((0, -100), pygame.Surface((WIDTH, 100)), RED))
# walls_h.add(Wall((0, HEIGHT), pygame.Surface((WIDTH, 100)), RED))
# walls_v_left.add(Wall((-100, -1000), pygame.Surface((100, 2000)), RED))
# walls_v_right.add(Wall((WIDTH, -1000), pygame.Surface((100, 2000)), RED))

# class Player(pygame.sprite.Sprite):
#     def __init__(self, pos, surface1, surface2, color, obj):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((surface1.get_rect().width, surface1.get_rect().height + surface2.get_rect().height))
#         x, y = pos
#         self.top = Part((x, y), surface1)
#         self.bottom = Part((x, y + surface1.get_rect().height), surface2)
#         self.image.fill(color)
#         self.rect = self.image.get_rect()
#         self.rect.topleft = pos
#         self.speed = 0.5
#         self.obj = obj
#         self.acc_value = pygame.Vector2(0.075, 0.2)
#         self.vel = pygame.Vector2(0, 0)
#         self.acc = pygame.Vector2(0, 0)
#         self.is_jump = True
#         self.x_vel = 0
#         self.y_vel = 0
#         x_vel = 0
#         y_vel = 0
#     def update(self):
#         global x_vel, y_vel
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_x] and self.is_jump:
#             self.acc.y = 12
#         if keys[pygame.K_s]:
#             self.acc.x = -10
#         if keys[pygame.K_w] and not self.is_jump:
#             self.acc.y = -12
#         if keys[pygame.K_d]:
#             self.vel.x = self.speed
#             self.acc.x += self.acc_value.x if (self.acc.x > 0) else 2 * self.acc_value.x
#         elif keys[pygame.K_a]:
#             self.vel.x = -self.speed
#             self.acc.x -= self.acc_value.x if (self.acc.x < 0) else 2 * self.acc_value.x
#         else:
#             self.vel.x = 0
#             if abs(self.acc.x) > self.acc_value.x:
#                 self.acc.x += -self.acc_value.x if (self.acc.x > 0) else self.acc_value.x
#             else:
#                 self.acc.x = 0
#         nw = (self.vel + self.acc)
#         self.x_vel = nw.x
#         self.y_vel = nw.y
#         x_vel = nw.x
#         y_vel = nw.y
#         # self.rect.center += (self.vel + self.acc)
#         # self.top.rect.center += (self.vel + self.acc)
#         # self.bottom.rect.center += (self.vel + self.acc)
#         # print(self.rect.center, self.top.rect.center, self.bottom.rect.center)
#         hit = (pygame.sprite.spritecollide(self.bottom, walls_h, False), pygame.sprite.spritecollide(self.top, walls_h, False))
#         if hit[1]:
#             self.is_jump = True
#             if self.acc.y < 0:
#                 self.acc.y = 0
#                 self.rect.top = hit[1][0].rect.bottom
#                 self.top.rect.top = hit[1][0].rect.bottom
#                 self.bottom.rect.top = hit[1][0].rect.bottom + self.top.rect.height
#         elif not hit[0]:
#             self.is_jump = True
#             self.acc.y += self.acc_value.y
#         else:
#             self.is_jump = False
#             self.rect.bottom = hit[0][0].rect.y
#             self.top.rect.bottom = hit[0][0].rect.y - self.top.rect.height
#             self.bottom.rect.bottom = hit[0][0].rect.y
#             self.acc.y = 0
#         hit = (pygame.sprite.spritecollide(self.bottom, self.obj, False), pygame.sprite.spritecollide(self.top, self.obj, False))
#         if hit[1]:
#             self.is_jump = True
#             if self.acc.y < 0:
#                 self.acc.y = 0
#                 self.rect.top = hit[1][0].rect.bottom
#                 self.top.rect.top = hit[1][0].rect.bottom
#                 self.bottom.rect.top = hit[1][0].rect.bottom + self.top.rect.height
#         elif not hit[0]:
#             self.is_jump = True
#             self.acc.y += self.acc_value.y
#         else:
#             self.is_jump = False
#             self.rect.bottom = hit[0][0].rect.y
#             self.top.rect.bottom = hit[0][0].rect.y - self.top.rect.height
#             self.bottom.rect.bottom = hit[0][0].rect.y
#             self.acc.y = 0
#         hit = pygame.sprite.spritecollide(self, walls_v_left, False)
#         if hit:
#             self.rect.left = hit[0].rect.right
#             self.top.rect.left = hit[0].rect.right
#             self.bottom.rect.left = hit[0].rect.right
#             self.acc.x = 0
#         hit = pygame.sprite.spritecollide(self, walls_v_right, False)
#         if hit:
#             self.rect.right = hit[0].rect.left
#             self.top.rect.right = hit[0].rect.left
#             self.bottom.rect.right = hit[0].rect.left
#             self.acc.x = 0
