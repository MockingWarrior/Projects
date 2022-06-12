import pygame

class SpriteSheet_9():
    def __init__(self,image):
        self.sheet = image

    def Animation_Player_One_Fifth(self, frame , width, height, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width), 149*2, width, height))
        image.set_colorkey(colour)

        return image

class SpriteSheet_10():
    def __init__(self,image):
        self.sheet = image

    def Animation_Player_Two_Fifth(self, frame , width, height, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((width*frame), 149*2, width, height))
        image.set_colorkey(colour)

        return image