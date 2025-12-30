import pygame

class Klocek(pygame.sprite.Sprite):
    def __init__(self, x, y, zdrowie):
        super(Klocek, self).__init__()
        self.obraz_oryginalny = pygame.image.load("images/brick.png")
        self.rect = pygame.Rect(x, y, 96, 48)
        self.zdrowie = zdrowie
        self.aktualizuj()

    def aktualizuj(self):
        maska_koloru = 0
        if self.zdrowie == 3:
            maska_koloru = (128, 0, 0)
        if self.zdrowie == 2:
            maska_koloru = (0, 0, 128)
        if self.zdrowie == 1:
            maska_koloru = (0, 128, 0)
        self.obraz = self.obraz_oryginalny.copy()
        self.obraz.fill(maska_koloru, special_flags=pygame.BLEND_ADD)

    def uderzenie(self):
        self.zdrowie -= 1
        if self.zdrowie <= 0:
            self.kill()