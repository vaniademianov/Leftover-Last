import pygame, grass_block as gb
grass_texture = pygame.image.load("res/tiles/grass_block.png")
grass_texture = pygame.transform.scale(grass_texture, (48,48))
class Ground(pygame.sprite.Sprite):
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
        player.add_inv(gb.Grass_block(1))
        self.kill()
    # def rl(self,pang,without=-1):
    #     pos = self.rect.topleft
    #     sprite_size = (grass_texture.get_width() * pang, grass_texture.get_height())
    #     grass_surface = pygame.Surface(sprite_size)
    #     self.grasses = []
    #     for x in range(pang):
    #         if x != without:
    #             for y in range(1):
    #                 self.grasses.append(pygame.Vector2(x=x, y=y))
    #                 grass_surface.blit(grass_texture, (x * grass_texture.get_width(), y * grass_texture.get_height()))
    #     self.image = grass_surface
    #     self.rang = pang
    #     self.rect = self.image.get_rect()
    #     self.rect.topleft = pos