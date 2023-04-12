import pygame, math
WIDTH = 800
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
eyes = pygame.image.load("res/eyes.png")
eyes = pygame.transform.scale(eyes, (eyes.get_width()/3,eyes.get_height()/3))
blue_img = pygame.image.load("res/blue.png")
blue_resized = pygame.transform.scale(blue_img, (blue_img.get_width()/5,blue_img.get_height()/5))
hit_img = pygame.image.load("res/hitbox.png")
hit_resized = pygame.transform.scale(hit_img, (hit_img.get_width()/9,hit_img.get_height()/7))
class Part(pygame.sprite.Sprite):
    def __init__(self, parent, pos,unt,img=hit_resized):
        self.image = img
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
    def __init__(self, pos, surface1, surface2, color, unt, scr):
        pygame.sprite.Sprite.__init__(self)
        x, y = pos
        self.image = blue_resized
        self.rect = self.image.get_rect()
        self.hitbox = Part(self,pos,unt)
        self.rect.topleft = pos
        self.speed = 1.5
        self.max_speed = 15
        self.screen = scr
        self.min_speed = -15
        self.is_jump = True
        self.x_vel = 0
        self.y_vel = 0
        self.unt = unt
        self.left=False
        self.is_breaking = True
        self.inv = [None, None, None,None,None,None,None,None,None,None]
        self.slot = 0
        self.walls_updated = 0
        self.eyes = Part(self, (self.rect.topleft[0]+self.rect.width/2, self.rect.topleft[1]-self.rect.height/3),self.unt,eyes)
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
        mouse_pos = pygame.mouse.get_pos()
        if self.x_vel == 0:
            
            xd = mouse_pos[0]-self.rect.x
            if xd<0 and self.left == False:
                self.t()
                self.left=True
            elif xd > 0 and self.left == True:
                self.t()
                self.left= False
        
        self.vel()
        dx = mouse_pos[0] - self.eyes.rect.x
        dy = mouse_pos[1] - self.eyes.rect.y
        angle = math.atan2(-dy, dx)

        rotated_eyes_surface = pygame.transform.rotate(self.eyes.image, math.degrees(angle))

        #self.screen.blit(rotated_eyes_surface, (self.rect.centerx-self.image.get_width()/2,self.rect.centery-self.image.get_width()/2))

    def vel(self):
        if self.x_vel<0 and self.left == False and self.is_breaking == False:
            self.t()
            self.left=True
        elif self.x_vel > 0 and self.left == True and self.is_breaking == False:
            self.t()
            self.left= False
    def t(self):
        self.image=pygame.transform.flip(self.image,flip_x=True, flip_y=False)
        self.eyes.image=pygame.transform.flip(self.eyes.image,flip_x=True, flip_y=False)
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