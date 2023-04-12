import pygame
pygame.init()
pickup = pygame.mixer.Sound("res/sounds/random/pop.ogg")
stone_1 = pygame.mixer.Sound("res/sounds/dig/stone1.ogg")
stone_2 = pygame.mixer.Sound("res/sounds/dig/stone2.ogg")
stone_3 = pygame.mixer.Sound("res/sounds/dig/stone3.ogg")
stone_4 = pygame.mixer.Sound("res/sounds/dig/stone4.ogg")
grass_1 = pygame.mixer.Sound("res/sounds/dig/grass1.ogg")
grass_2 = pygame.mixer.Sound("res/sounds/dig/grass2.ogg")
grass_3 = pygame.mixer.Sound("res/sounds/dig/grass3.ogg")
grass_4 = pygame.mixer.Sound("res/sounds/dig/grass4.ogg")
def play(sound):
    sound.play()