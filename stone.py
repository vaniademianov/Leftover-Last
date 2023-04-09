import pygame, coblestone_block as sb
grass_texture = pygame.image.load("res/tiles/stone_block.png")
grass_texture = pygame.transform.scale(grass_texture, (48,48))
class Stone(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = grass_texture
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    # def get_nearest(x,y):
    #     return (x/grass_texture.get_width(),y/grass_texture.get_height())
    def update(self, plauer):
        self.rect.x += -plauer.x_vel
        self.rect.y += -plauer.y_vel
    def brek(self, player):
        player.add_inv(sb.Stone_block(1))
        self.kill()