import random

import pygame
pygame.init()
#ustawianie wielkości okna
szerokosc = 1200
wysokosc = 550
screen = pygame.display.set_mode((szerokosc,wysokosc))

dlugosc_paletki = 90
szerokosc_paletki = 20
paletka_x = 25
paletka_prawa_y = wysokosc/2-dlugosc_paletki/2
paletka_lewa_y = wysokosc / 2 - dlugosc_paletki / 2

grubosc_lini = 20
linia = pygame.rect.Rect(szerokosc / 2 - grubosc_lini / 2, 0, grubosc_lini, wysokosc)

rozmiar_pileczki = 20
polozenie_pileczki_y = wysokosc / 2 - rozmiar_pileczki / 2# na jakiej wyskości piłeczka się znajduje
polozenie_pileczki_x = szerokosc / 2 - rozmiar_pileczki / 2#jak daleko od ściany piłeczka się znajduje
level = int(input("chose the level of difficulty from 1 to 4"))

ball_speed_choices = []

predkosc_x = 0
predkosc_y = 0
HP_left = 0
HP_right = 0

if level == 1:
    predkosc_x = random.randint(0,1)
    predkosc_y = random.randint(0,1)
    if predkosc_x == 1:
        predkosc_x = 3
    if predkosc_x == 0:
        predkosc_x = -3
    if predkosc_y == 1:
        predkosc_y = 3
    if predkosc_y == 0:
        predkosc_y = -3
    HP_left = 5
    HP_right = 5

if level == 2:
    predkosc_x = random.randint(0, 1)
    predkosc_y = random.randint(0, 1)
    if predkosc_x == 1:
        predkosc_x = 4
    if predkosc_x == 0:
        predkosc_x = -4
    if predkosc_y == 1:
        predkosc_y = 4
    if predkosc_y == 0:
        predkosc_y = -4
    HP_left = 4
    HP_right = 4

if level == 3:
    predkosc_x = random.randint(0, 1)
    predkosc_y = random.randint(0, 1)
    if predkosc_x == 1:
        predkosc_x = 5
    if predkosc_x == 0:
        predkosc_x = -5
    if predkosc_y == 1:
        predkosc_y = 5
    if predkosc_y == 0:
        predkosc_y = -5
    HP_left = 3
    HP_right = 3

if level == 4:
    predkosc_x = random.randint(0, 1)
    predkosc_y = random.randint(0, 1)
    if predkosc_x == 1:
        predkosc_x = 6
    if predkosc_x == 0:
        predkosc_x = -6
    if predkosc_y == 1:
        predkosc_y = 6
    if predkosc_y == 0:
        predkosc_y = -6
    HP_left = 2
    HP_right = 2


#random.randint(-6,6)
nazwa_gracza_lewo = input("user name from left side")
nazwa_gracza_prawo = input("user name from right side")
points_left = 0
points_right = 0

def show_lobby (screen:pygame.Surface):
    screen.fill('black')
def game():
    # rysowanie obiektów na planszy
    pygame.draw.rect(screen, 'white', linia)
    paletka_lewa = pygame.rect.Rect(
        paletka_x,
        paletka_lewa_y,
        szerokosc_paletki,
        dlugosc_paletki)
    pygame.draw.rect(screen, 'white', paletka_lewa)
    paletka_prawa = pygame.rect.Rect(
        szerokosc - (szerokosc_paletki + paletka_x),
        paletka_prawa_y,
        szerokosc_paletki,
        dlugosc_paletki)
    pygame.draw.rect(screen, 'white', paletka_prawa)
    pileczka = pygame.rect.Rect(
        polozenie_pileczki_x,
        polozenie_pileczki_y,
        rozmiar_pileczki,
        rozmiar_pileczki)
    pygame.draw.rect(screen, 'red', pileczka)
    # pisanie nicku gracza
    gracz_lewo_name_render = font.render(f'{nazwa_gracza_lewo} Points: {points_left}', True, 'white')
    gracz_prawo_name_render = font.render(f'{nazwa_gracza_prawo} Points: {points_right}', True, 'white')
    screen.blit(gracz_lewo_name_render, (paletka_x, 10), )
    szerokosc_nicku_gracza_prawo = gracz_prawo_name_render.get_width()
    screen.blit(gracz_prawo_name_render, (szerokosc - szerokosc_nicku_gracza_prawo - 10, 10), )

    gracz_prawo_HP_render = font.render(f'HP:{HP_right}', True, 'white')
    szerokosc_HP_gracza_prawo = gracz_prawo_HP_render.get_width()
    screen.blit(gracz_prawo_HP_render, (szerokosc - szerokosc_HP_gracza_prawo - 10, 60), )

    gracz_lewo_HP_render = font.render(f'HP:{HP_left}', True, 'white')
    szerokosc_HP_gracza_lewo = gracz_lewo_HP_render.get_width()
    screen.blit(gracz_lewo_HP_render, (paletka_x, 60), )

    # obsługa eventów
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # poruszanie obiektami
    klawa = pygame.key.get_pressed()
    if klawa[pygame.K_DOWN]:
        paletka_prawa_y += 8
        if paletka_prawa_y >= 550 - dlugosc_paletki:
            paletka_prawa_y = 550 - dlugosc_paletki
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
        if paletka_lewa_y >= 550 - dlugosc_paletki:
            paletka_lewa_y = 550 - dlugosc_paletki
    # zmina miejsca piłeczki
    polozenie_pileczki_x += predkosc_x
    polozenie_pileczki_y += predkosc_y
    if polozenie_pileczki_y >= wysokosc - 20:
        predkosc_y = predkosc_y * -1
    if polozenie_pileczki_y <= 0:
        predkosc_y = predkosc_y * -1
    if polozenie_pileczki_x >= szerokosc - 20:
        predkosc_x = predkosc_x * -1
    if polozenie_pileczki_x <= 0:
        predkosc_x = predkosc_x * -1

    if polozenie_pileczki_x >= paletka_x and polozenie_pileczki_x <= paletka_x + szerokosc_paletki and polozenie_pileczki_y <= paletka_lewa_y + dlugosc_paletki and polozenie_pileczki_y >= paletka_lewa_y:
        predkosc_x = predkosc_x * -1
        points_left += 1

    if polozenie_pileczki_x <= szerokosc - paletka_x:
        if polozenie_pileczki_x + rozmiar_pileczki >= szerokosc - paletka_x - szerokosc_paletki:  # sprawdzamy polożenie lewej krawędzi paletki i prawej krawędzi piłeczki
            if polozenie_pileczki_y <= paletka_prawa_y + dlugosc_paletki:  # sprawdzamy kolizję z dolną krawędzią
                if polozenie_pileczki_y + rozmiar_pileczki >= paletka_prawa_y:  # sprawdzamy kolizję z górną krawędzią.
                    predkosc_x = predkosc_x * -1
                    points_right += 1


zegarek = pygame.time.Clock()
font = pygame.font.Font(size = 60)


while True:
    zegarek.tick(60)
    screen.fill('black')

    pygame.display.update()












