import pygame

class SpriteSheet_1():
    def __init__(self,image):
        self.sheet = image

    def Animation_Player_One_First(self, frame , width, height, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width), 149, width, height))
        image.set_colorkey(colour)

        return image

class SpriteSheet_5():
    def __init__(self,image):
        self.sheet = image

    def Animation_Player_Two_First(self, frame , width, height, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width), 149, width, height))
        image.set_colorkey(colour)

        return image
    