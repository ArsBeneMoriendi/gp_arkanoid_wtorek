import pygame
from Platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek
import time

WYSOKOSC_EKRANU = 800 #400
SZEROKOSC_EKRANU = 1024 #512
Zycia = 3
Poziom = 0

#poziomy gry
poziom1 = [
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

poziom2 = [
    [0, 0, 1, 2, 3, 3, 2, 1, 0, 0],
    [0, 1, 1, 1, 2, 2, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 2, 0, 2, 0]
]
poziom3 = [
    [2, 3, 2, 2, 2, 2, 2, 2, 3, 2],
    [2, 1, 3, 1, 1, 1, 1, 3, 1, 2],
    [2, 3, 1, 3, 1, 1, 3, 1, 3, 2],
    [3, 2, 2, 2, 3, 3, 2, 2, 2, 3],
    [0, 0, 2, 2, 3, 3, 2, 2, 0, 0],
    [0, 0, 2, 0, 3, 3, 0, 2, 0, 0],
    [0, 0, 3, 0, 3, 3, 0, 3, 0, 0]
]


ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

platforma = Platforma()
kulka = Kulka()

klocki = pygame.sprite.Group()
def dodaj_klocki():
    wczytany_poziom = None
    if Poziom == 0:
        wczytany_poziom = poziom1
    if Poziom == 1:
        wczytany_poziom = poziom2
    if Poziom == 2:
        wczytany_poziom = poziom3
    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32+i*96, 32+j*48, wczytany_poziom[j][i])
                klocki.add(klocek)
dodaj_klocki()

gra_dziala = True 
while gra_dziala: 
    for zdarzenie in pygame.event.get(): 
        if zdarzenie.type == pygame.KEYDOWN: 
            if zdarzenie.key == pygame.K_ESCAPE: 
                gra_dziala = False 
        elif zdarzenie.type == pygame.QUIT: 
            gra_dziala = False 


    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]: 
        platforma.ruszaj_platforma(-1) 
    if keys[pygame.K_RIGHT]: 
        platforma.ruszaj_platforma(1) 

    if len(klocki.sprites()) == 0:
        Poziom += 1
        if Poziom >= 3:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()

    kulka.aktualizuj(platforma, klocki)
    platforma.aktualizuj()

    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            break
        time.sleep(1)
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    ekran.blit(obraz_tla, (0,0)) 
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.pozycja)

    for k in klocki:
        ekran.blit(k.obraz, k.rect)

    pygame.display.flip() 
    zegar.tick(30) 
pygame.quit()