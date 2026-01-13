import pygame
import random

WYSOKOSC_EKRANU = 800
SZEROKOSC_EKRANU = 1024

vec = pygame.math.Vector2

class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super(Kulka, self).__init__()
        self.obraz = pygame.image.load("images/ball.png")
        self.r = 16
        self.przegrana = False
        self.zresetuj_pozycje()

    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU-150)
        self.pozycja = self.obraz.get_rect(center = self.wspolrzedne)
        self.wektor = vec(0, -10)
        self.kat_nachylenia = random.randrange(-30, 30)
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False
    
    def aktualizuj(self, platforma, klocki):
        self.wspolrzedne += self.wektor
        self.pozycja.center = self.wspolrzedne
        self.sprawdz_kolizje(platforma, klocki)

    def sprawdz_kolizje(self, platforma, klocki):
        if self.pozycja.x <= 0:
            self.wektor.x *=-1
        if self.pozycja.right >= SZEROKOSC_EKRANU:
            self.wektor.x *=-1
        if self.pozycja.top <= 0:
            self.wektor.y *=-1
        if self.pozycja.bottom >= WYSOKOSC_EKRANU:
            self.przegrana = True

        if self.pozycja.colliderect(platforma.rect):
            self.wektor.y *=-1
            self.wektor.x += platforma.porusza_sie*5
            if self.wektor.x <-10: self.wektor.x =-10
            if self.wektor.x > 10: self.wektor.x = 10

        #kolizja z klockami
        for klocek in klocki:
            #nastąpiła kolizja
            if self.kolizja_z_klockiem(self, klocek):
                klocek.uderzenie()

    #metoda pomocnicza do kolizji z klockiem
    def kolizja_z_klockiem(self, kulka, klocek):
        dystans_x = abs(kulka.pozycja.centerx - klocek.rect.centerx) - klocek.rect.w / 2
        dystans_y = abs(kulka.pozycja.centery - klocek.rect.centery) - klocek.rect.h / 2
        if dystans_x < kulka.r and dystans_y < kulka.r:
            if dystans_x < dystans_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1
            return True
        return False