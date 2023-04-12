import pygame, coblestone_block as sb, random, mixer as mx
grass_texture = pygame.image.load("res/tiles/stone_block.png")
small = pygame.transform.scale(grass_texture, (16,16))
grass_texture = pygame.transform.scale(grass_texture, (48,48))

class Stone(pygame.sprite.Sprite):
    def __init__(self, pos, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = grass_texture
        self.rect = self.image.get_rect()
        self.daughter = sb.Stone_block
        self.rect.topleft = pos
        self.player = player
        self.i = 0
        self.w = 0
    # def get_nearest(x,y):
    #     return (x/grass_texture.get_width(),y/grass_texture.get_height())
    def update(self, plauer,x_vel,y_vel):
        self.i += 2
        self.rect.y += self.w
        if pygame.sprite.spritecollide(self, plauer.unt, False):
            self.w = 0
        self.rect.x += -x_vel
        self.rect.y += -y_vel
        self.rect.move(self.rect.x+(-x_vel), self.rect.y+(-y_vel))
        # print("MOVED BY: ",-x_vel,"fps:",self.i)
        return True
    def brek(self, player, group):
    # Teleport the sprite to the bottom center of the screen
        # self.rect.centery += self.image.get_height() // 2
        self.w = 1
        self.rect.centerx += self.image.get_height() // 2
    # Replace the sprite image with the bigger one and adjust its rect
        self.image = small
        self.rect.size = small.get_size()
        mx.play(random.choice([mx.stone_1,mx.stone_2,mx.stone_3,mx.stone_4]))
        # player.add_inv(sb.Stone_block(1))
        self.kill()
        group.add(self)