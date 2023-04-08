import pygame
txt = []
for a in range(0,10,1):
    txt.append(pygame.image.load("res/destroy_stages/destroy_stage_" + str(a)+".png"))
    txt[a] = pygame.transform.scale(txt[a], (48,48))
FPS=30
class Break(pygame.sprite.Sprite):
    def __init__(self, pos, perent, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = txt[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.runn = 0
        self.st = 0
        self.change_stage_every = 0.1
        self.perent = perent 
        self.player = player
        self.player.is_breaking = True
    def update(self) -> None:
        self.runn+=1

        if self.runn%(self.change_stage_every*FPS) == 0:
            self.st+=1
            self.image = txt[self.st]
            self.runn = 0
        if (self.st >= 9):
            self.perent.brek(self.player)
            self.player.is_breaking = False
            self.kill()
        if not self.player.is_breaking:
            self.kill()