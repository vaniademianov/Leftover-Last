import pygame, grass_block as gb, mixer as mx, random
grass_texture = pygame.image.load("res/tiles/grass_block.png")
grass_texture = pygame.transform.scale(grass_texture, (48,48))
grass_texture = pygame.transform.flip(grass_texture, False,True)
small = pygame.transform.scale(grass_texture, (16,16))
class Ground(pygame.sprite.Sprite):
    def __init__(self, pos, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = grass_texture
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.daughter = gb.Grass_block
        self.player = player
        self.i = 0
        self.w = 0
    # def get_nearest(x,y):
    #     return (x/grass_texture.get_width(),y/grass_texture.get_height())
    def update(self, plauer,x_vel,y_vel):
        self.i += 1
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
        mx.play(random.choice([mx.grass_1,mx.grass_2,mx.grass_3,mx.grass_4]))
        self.rect.size = small.get_size()
        # player.add_inv(sb.Stone_block(1))
        self.kill()
        group.add(self)