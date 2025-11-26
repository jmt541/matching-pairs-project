import pygame

class Card:
    kartuBelakang = None
    kartuBelakangPath = "asset/card/card-back.png"

    @classmethod
    def load_assets(cls, kartuBelakangPath):
        cls.kartuBelakang = pygame.image.load(kartuBelakangPath)


    def __init__(self, kartuDepanPath, value, x, y):
        self.kartuDepan = pygame.image.load(kartuDepanPath)
        self.rect = self.kartuDepan.get_rect(topleft=(x,y))
        self.value = value
        self.flipped = False
        self.matched = False


    def draw(self, screen):
        if self.flipped or self.matched:
            screen.blit(self.kartuDepan, self.rect)

        else:
            screen.blit(Card.kartuBelakang, self.rect)




            




