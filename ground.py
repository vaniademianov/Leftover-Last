import pygame
grass_texture = pygame.image.load("res/tiles/grass_block.png")
grass_texture = pygame.transform.scale(grass_texture, (48,48))
class Ground(pygame.sprite.Sprite):
    def __init__(self, pos,pang):
        pygame.sprite.Sprite.__init__(self)
        sprite_size = (grass_texture.get_width() * pang, grass_texture.get_height())
        grass_surface = pygame.Surface(sprite_size)
        for x in range(pang):
            for y in range(1):
                grass_surface.blit(grass_texture, (x * grass_texture.get_width(), y * grass_texture.get_height()))
        self.image = grass_surface
        self.rang = pang
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def update(self, plauer):
        self.rect.x += -plauer.x_vel
        self.rect.y += -plauer.y_vel
