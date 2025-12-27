import pygame
from Platforma import Platforma
from Kulka import Kulka

WYSOKOSC_EKRANU = 800 #400
SZEROKOSC_EKRANU = 1024 #512

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

platforma = Platforma()
kulka = Kulka()

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

    kulka.aktualizuj(platforma)
    platforma.aktualizuj()

    ekran.blit(obraz_tla, (0,0)) 
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.pozycja)

    pygame.display.flip() 
    zegar.tick(30) 
pygame.quit()