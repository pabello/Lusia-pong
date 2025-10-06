import random
import pygame


pygame.init()

################================---------------- INICJALIZACJA STAŁYCH I ZMIENNYCH ----------------================################
font = pygame.font.Font(size = 60)

# Ustawiania wielkości okna
SZEROKOSC = 1200
WYSOKOSC = 550
screen = pygame.display.set_mode((SZEROKOSC,WYSOKOSC))

# Ustawienia paletek
DLUGOSC_PALETKI = 90
SZEROKOSC_PALETKI = 20
DYSTANS_PALETKI_OD_SCIANY = 25
paletka_prawa_y = (WYSOKOSC / 2) - (DLUGOSC_PALETKI / 2)
paletka_lewa_y = (WYSOKOSC / 2) - (DLUGOSC_PALETKI / 2)

# Ustawienia linii środkowej
GRUBOSC_LINII = 20
linia = pygame.rect.Rect((SZEROKOSC / 2) - (GRUBOSC_LINII / 2), 0, GRUBOSC_LINII, WYSOKOSC)

# Ustawienia piłeczki
ROZMIAR_PILECZKI = 20
polozenie_pileczki_y = (WYSOKOSC / 2) - (ROZMIAR_PILECZKI / 2)  # Na jakiej wyskości piłeczka się znajduje
polozenie_pileczki_x = (SZEROKOSC / 2) - (ROZMIAR_PILECZKI / 2)  # Jak daleko od ściany piłeczka się znajduje


# Ustawienia poziomu trudności (szybkość piłeczki i ilość HP)
"""
Żeby można było wybrać poziom trudności klikając w ekranie lobby, musimy przenieść ten kod do nowej funkcji
"""
level = int(input("Chose the level of difficulty from 1 to 4: "))

HP_left = 6 - level
HP_right = 6 - level

predkosc_x = random.choice([-1,1])
predkosc_y = random.randint(-1,1)

if level == 1:  # Level easy
    predkosc_x = predkosc_x * 4
    predkosc_y = predkosc_y * 4

if level == 2:  # Level medium
    predkosc_x = predkosc_x * 5
    predkosc_y = predkosc_y * 5

if level == 3:  # Level hard
    predkosc_x = predkosc_y * 6
    predkosc_y = predkosc_y * 6

if level == 4:  # Level hell
    predkosc_x = predkosc_y * 10
    predkosc_y = predkosc_y * 10
"""Aż dotąd"""

# Ustawienia graczy
nazwa_gracza_lewo = "Player 1"
nazwa_gracza_prawo = "Player 2"
# nazwa_gracza_lewo = input("user name from left side")
# nazwa_gracza_prawo = input("user name from right side")
points_left = 0
points_right = 0

################================---------------- EKRANY GRY ----------------================################

# Ekran lobby
def show_lobby (screen:pygame.Surface):
    screen.fill('black')


# Ekran widoku gry
def game():
    """
    Tutaj zamiast komentarza, trzeba dodać wczytanie zmiennych globalnychs
    """

    pygame.draw.rect(screen, 'white', linia)

    paletka_lewa = pygame.rect.Rect(
        DYSTANS_PALETKI_OD_SCIANY,
        paletka_lewa_y,
        SZEROKOSC_PALETKI,
        DLUGOSC_PALETKI)
    paletka_prawa = pygame.rect.Rect(
        SZEROKOSC - (SZEROKOSC_PALETKI + DYSTANS_PALETKI_OD_SCIANY),
        paletka_prawa_y,
        SZEROKOSC_PALETKI,
        DLUGOSC_PALETKI)
    pygame.draw.rect(screen, 'white', paletka_lewa)
    pygame.draw.rect(screen, 'white', paletka_prawa)

    pileczka = pygame.rect.Rect(
        polozenie_pileczki_x,
        polozenie_pileczki_y,
        ROZMIAR_PILECZKI,
        ROZMIAR_PILECZKI)
    pygame.draw.rect(screen, 'red', pileczka)

    # Wyświetlanie nicków i punktów
    gracz_lewo_name_render = font.render(f'{nazwa_gracza_lewo} Points: {points_left}', True, 'white')
    gracz_prawo_name_render = font.render(f'{nazwa_gracza_prawo} Points: {points_right}', True, 'white')
    szerokosc_nicku_gracza_prawo = gracz_prawo_name_render.get_width()
    screen.blit(gracz_lewo_name_render, (DYSTANS_PALETKI_OD_SCIANY, 10), )
    screen.blit(gracz_prawo_name_render, (SZEROKOSC - szerokosc_nicku_gracza_prawo - 10, 10), )

    # Wyświetlanie HP
    gracz_prawo_HP_render = font.render(f'HP:{HP_right}', True, 'white')
    szerokosc_HP_gracza_prawo = gracz_prawo_HP_render.get_width()
    gracz_lewo_HP_render = font.render(f'HP:{HP_left}', True, 'white')

    screen.blit(gracz_prawo_HP_render, (SZEROKOSC - szerokosc_HP_gracza_prawo - 10, 60), )
    screen.blit(gracz_lewo_HP_render, (DYSTANS_PALETKI_OD_SCIANY, 60), )


    # Poruszanie paletkami
    klawa = pygame.key.get_pressed()
    if klawa[pygame.K_DOWN]:
        paletka_prawa_y += 8
        if paletka_prawa_y >= 550 - DLUGOSC_PALETKI:
            paletka_prawa_y = 550 - DLUGOSC_PALETKI
    if klawa[pygame.K_UP]:
        paletka_prawa_y -= 8
        if paletka_prawa_y <= 0:
            paletka_prawa_y = 0
    if klawa[pygame.K_w]:
        paletka_lewa_y -= 8
        if paletka_lewa_y <= 0:
            paletka_lewa_y = 0
    if klawa[pygame.K_s]:
        paletka_lewa_y += 8
        if paletka_lewa_y >= 550 - DLUGOSC_PALETKI:
            paletka_lewa_y = 550 - DLUGOSC_PALETKI

    # Aktualizacja położenia piłeczki
    polozenie_pileczki_x += predkosc_x
    polozenie_pileczki_y += predkosc_y

    # Sprawdzanie kolizji piłeczki ze ścianami i paletkami
    if polozenie_pileczki_y >= WYSOKOSC - ROZMIAR_PILECZKI:
        predkosc_y = predkosc_y * -1
    elif polozenie_pileczki_y <= 0:
        predkosc_y = predkosc_y * -1

    if polozenie_pileczki_x >= SZEROKOSC - ROZMIAR_PILECZKI:
        predkosc_x = predkosc_x * -1
    elif polozenie_pileczki_x <= 0:
        predkosc_x = predkosc_x * -1

    # Kolizja piłeczki z lewą paletką
    if polozenie_pileczki_x >= DYSTANS_PALETKI_OD_SCIANY and \
            polozenie_pileczki_x <= DYSTANS_PALETKI_OD_SCIANY + SZEROKOSC_PALETKI and \
            polozenie_pileczki_y <= paletka_lewa_y + DLUGOSC_PALETKI and \
            polozenie_pileczki_y >= paletka_lewa_y:
        predkosc_x = predkosc_x * -1
        points_left += 1

    # Kolizja piłeczki z prawą paletką
    if polozenie_pileczki_x <= SZEROKOSC - DYSTANS_PALETKI_OD_SCIANY:  # Pileczka po lewo od prawej paletki
        if polozenie_pileczki_x + ROZMIAR_PILECZKI >= SZEROKOSC - DYSTANS_PALETKI_OD_SCIANY - SZEROKOSC_PALETKI:  # Prawa krawędź piłeczki i lewa krawędź paletki
            if polozenie_pileczki_y <= paletka_prawa_y + DLUGOSC_PALETKI:  # Czy piłeczka nie jest poniżej paletki
                if polozenie_pileczki_y + ROZMIAR_PILECZKI >= paletka_prawa_y:  # Czy piłeczka nie jest powyżej paletki
                    predkosc_x = predkosc_x * -1
                    points_right += 1


##################################################################################################################
################================---------------- GŁÓWNA PĘTLA GRY ----------------================################
##################################################################################################################

wylacz_gre = False
tryb_gry = "game"  # lobby, game, score, end
zegarek = pygame.time.Clock()
while wylacz_gre == False:
    zegarek.tick(60)
    screen.fill('black')

    # Obsługa eventów
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wylacz_gre = True

    if tryb_gry == "game":
        game()

    pygame.display.update()

