import pygame, ground as g
class Grass_block:
    def __init__(self, count) -> None:
        self.type = "Grass_block"
        self.count = count
        self.mini = pygame.transform.scale(pygame.image.load("res/tiles/grass_block.png"), (32,32))
        self.parent_block = g.Ground
        