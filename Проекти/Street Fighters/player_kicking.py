import pygame

class SpriteSheet_11():
    def __init__(self,image):
        self.sheet = image

    def Animation_Player_One_Sixth(self, frame , width, height, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width), 149*6, width, height))
        image.set_colorkey(colour)

        return image

class SpriteSheet_12():
    def __init__(self,image):
        self.sheet = image

    def Animation_Player_Two_Sixth(self, frame , width, height, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((width*frame), 149*6, width, height))
        image.set_colorkey(colour)

        return image