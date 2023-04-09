import pygame, stone as g
class Stone_block:
    def __init__(self, count) -> None:
        self.type = "Coblestone_block"
        self.count = count
        self.mini = pygame.transform.scale(pygame.image.load("res/tiles/cobblestone.png"), (32,32))
        self.parent_block = g.Stone
        