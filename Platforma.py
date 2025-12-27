import pygame

WYSOKOSC_EKRANU = 800 #400
SZEROKOSC_EKRANU = 1024 #512

class Platforma(pygame.sprite.Sprite):
    def __init__(self):
        super(Platforma, self).__init__()
        self.obraz = pygame.image.load("images/pad.png")
        self.porusza_sie = 0
        self.zresetuj_pozycje()

    def zresetuj_pozycje(self):
        self.rect = pygame.Rect(SZEROKOSC_EKRANU/2-70, WYSOKOSC_EKRANU*0.85, 140, 30)

    def ruszaj_platforma(self, wartosc): 
        predkosc = 10 
        self.porusza_sie = wartosc
        self.rect.move_ip(wartosc*predkosc, 0) 
        if self.rect.left <= 0: self.rect.x = 0 
        if self.rect.right >= SZEROKOSC_EKRANU: self.rect.x = SZEROKOSC_EKRANU-140 

    def aktualizuj(self):
        self.porusza_sie = 0