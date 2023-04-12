import pygame, coblestone_block as sb, random, mixer as mx, numpy as np,utils as ut
grass_texture = pygame.image.load("res/tiles/stone_block.png")
small = pygame.transform.scale(grass_texture, (16,16))
grass_texture = pygame.transform.scale(grass_texture, (48,48))

class Stone(pygame.sprite.Sprite):
    def __init__(self, pos, player):
        pygame.sprite.Sprite.__init__(self)
        self.brightness = 0.8
        self.image = grass_texture.convert_alpha() 
        self.image.set_alpha(int(self.brightness * 255))
        self.rect = self.image.get_rect()
        self.daughter = sb.Stone_block
        self.rect.topleft = pos
        self.player = player
        self.w = 0
        self.bk = False
    # def get_nearest(x,y):
    #     return (x/grass_texture.get_width(),y/grass_texture.get_height())
    def update(self, plauer,x_vel,y_vel):
        self.brightness = 0.7-(ut.calc_dist(self.rect.x, self.rect.y, plauer.rect.x, plauer.rect.y)/480)
        self.image.set_alpha(int(self.brightness * 255))
        self.rect.y += self.w
        if pygame.sprite.spritecollide(self, plauer.unt, False) and self.bk:
            self.w = 0
        elif not pygame.sprite.spritecollide(self, plauer.unt, False) and self.bk:
            self.w = 1
        self.rect.x += -x_vel
        self.rect.y += -y_vel
        self.rect.move(self.rect.x+(-x_vel), self.rect.y+(-y_vel))
        # print("MOVED BY: ",-x_vel,"fps:",self.i)
        return True
    def brek(self, player, group):
    # Teleport the sprite to the bottom center of the screen
        # self.rect.centery += self.image.get_height() // 2
        self.w = 1
        self.bk = True
        self.rect.centerx += self.image.get_height() // 2
    # Replace the sprite image with the bigger one and adjust its rect
        self.image = small
        self.rect.size = small.get_size()
        mx.play(random.choice([mx.stone_1,mx.stone_2,mx.stone_3,mx.stone_4]))
        # player.add_inv(sb.Stone_block(1))
        self.kill()
        group.add(self)