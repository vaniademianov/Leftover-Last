import pygame
slot_txt = pygame.image.load("res/slot_act.png")
slot_act_txt = pygame.transform.scale(slot_txt,(80,80))
class Slot(pygame.sprite.Sprite):
    def __init__(self, pos, number,player):
        pygame.sprite.Sprite.__init__(self)
        x, y = pos
        self.number = number
        self.player = player
        self.image = slot_txt
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos
        self.min = None
        self.state = False
    def update(self, scr) -> None:
        sprite2_x, sprite2_y = self.rect.topright    
        if self.player.inv[self.number] != None:

            scr.blit(self.player.inv[self.number].mini,((sprite2_x+(slot_txt.get_width()/6))-slot_txt.get_width(), sprite2_y+(slot_txt.get_height()/8)))
        # if not self.player.inv[self.number] == None and self.min != self.player.inv[self.number].mini:
            
        #     if self.player.inv[self.number] != None:
        #         self.min = self.player.inv[self.number].mini
        #         self.image.blit(self.player.inv[self.number].mini, self.rect.center)
        # if self.player.slot == self.number and not self.state:
        #     self.image = slot_act_txt
        #     self.state = True
        #     if self.player.inv[self.number] != None:
        #         self.min = self.player.inv[self.number].mini
        #         self.image.blit(self.player.inv[self.number].mini, self.rect.center)
        # if self.player.slot != self.number and self.state:
        #     self.image = slot_txt
        #     self.state = False
        #     if self.player.inv[self.number] != None:
        #         self.min = self.player.inv[self.number].mini
        #         self.image.blit(self.player.inv[self.number].mini, self.rect.center)