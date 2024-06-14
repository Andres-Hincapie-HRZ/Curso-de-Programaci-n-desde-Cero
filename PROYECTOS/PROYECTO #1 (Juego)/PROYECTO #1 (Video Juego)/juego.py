# Importar librerias necesarias
import math
import random
import pygame
from pygame import mixer

# Inicializar libreria pygame
pygame.init()
# Crear la pantalla del juego
pantalla = pygame.display.set_mode((900, 600))

# Establecer imagen de fodo del juego
fondo = pygame.image.load('fondo.png')

# Establecer musica de fondo del juego
mixer.music.load("musica_fondo.wav")
mixer.music.play(-1)

# Título del juego y el Icono del juego
pygame.display.set_caption("IRON MAN EN EL ESPACIO")
icono = pygame.image.load('icono.ico')
pygame.display.set_icon(icono)

# Establecer jugador (imagen 64x64 formato png) + movimientos del Jugador
jugador_img = pygame.image.load('jugador.png')
jugadorX = 370
jugadorY = 480
jugadorX_cambio = 0

# Establecer Enemigo y movimientos del enemigo y cantidad de enemigos
enemigo_img = []
enemigoX = []
enemigoY = []
enemigoX_cambio = []
enemigoY_cambio = []
num_de_enemigos = 6
# Movimiento del enemigo de izquierda a derecha  (imagen 70x70 formato png)
for i in range(num_de_enemigos):
    enemigo_img.append(pygame.image.load('enemigo.png'))
    enemigoX.append(random.randint(0, 736))
    enemigoY.append(random.randint(50, 150))
    enemigoX_cambio.append(1)  # Reducimos la velocidad de movimiento horizontal de los enemigos
    enemigoY_cambio.append(40)

# Establecer coete o bala (imagen 32x32 formato png) + movimiento vertical de las balas
bala_img = pygame.image.load('bala.png')
balas = []
balaY_cambio = 2  

# Puntuación del jugador
valor_puntuacion = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
textoX = 10
textoY = 10

# Pantalla final Game Over 
fuente_game_over = pygame.font.Font('freesansbold.ttf', 64)

def mostrar_puntuacion(x, y):
    puntuacion = fuente.render("PUNTAJE : " + str(valor_puntuacion), True, (255, 255, 255))
    pantalla.blit(puntuacion, (x, y))

def texto_game_over():
    texto_game_over = fuente_game_over.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(texto_game_over, (200, 250))

def jugador(x, y):
    pantalla.blit(jugador_img, (x, y))

def enemigo(x, y, i):
    pantalla.blit(enemigo_img[i], (x, y))

def disparar_bala(x, y):
    bala = {'x': x, 'y': y}
    balas.append(bala)

def colision(enemigoX, enemigoY, balaX, balaY):
    distancia = math.sqrt(math.pow(enemigoX - balaX, 2) + (math.pow(enemigoY - balaY, 2)))
    if distancia < 27:
        return True
    else:
        return False

# Bucles del juego
jugando = True
while jugando:
    pantalla.fill((0, 0, 0))
    pantalla.blit(fondo, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        # Detección de teclas para moverse y disparar 
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorX_cambio = -2  
            if evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 2  
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.wav")
                sonido_bala.play()
                balaX = jugadorX
                disparar_bala(balaX, jugadorY)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 0

    # Movimiento del jugador (dentro de bucles del juego)
    jugadorX += jugadorX_cambio
    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 736:
        jugadorX = 736

    # Movimiento de los enemigos y colisión al impacto de la bala (dentro de bucles del juego)
    for i in range(num_de_enemigos):
        if enemigoY[i] > 440:
            for j in range(num_de_enemigos):
                enemigoY[j] = 2000
            texto_game_over()
            break

        enemigoX[i] += enemigoX_cambio[i]
        if enemigoX[i] <= 0:
            enemigoX_cambio[i] = 1  # Reducimos la velocidad de movimiento horizontal de los enemigos
            enemigoY[i] += enemigoY_cambio[i]
        elif enemigoX[i] >= 736:
            enemigoX_cambio[i] = -1  # Reducimos la velocidad de movimiento horizontal de los enemigos
            enemigoY[i] += enemigoY_cambio[i]

        # Impacto de las balas en los enemigos + (sonido duracion 1segundo max 2 fotmato wav) (dentro de bucles del juego)
        for bala in balas:
            colisiona = colision(enemigoX[i], enemigoY[i], bala['x'], bala['y'])
            if colisiona:
                sonido_explosion = mixer.Sound("explosion.wav")
                sonido_explosion.play()
                balas.remove(bala)
                valor_puntuacion += 1
                enemigoX[i] = random.randint(0, 736)
                enemigoY[i] = random.randint(50, 150)
                break

        enemigo(enemigoX[i], enemigoY[i], i)

    # Movimiento y renderizado de las balas (dentro de bucles del juego)
    for bala in balas:
        bala['y'] -= balaY_cambio
        pantalla.blit(bala_img, (bala['x'] + 16, bala['y'] + 10))

    # Eliminar balas fuera de pantalla (dentro de bucles del juego)
    for bala in balas.copy():
        if bala['y'] <= 0:
            balas.remove(bala)
            
    # Mostrar jugador y puntuacion
    jugador(jugadorX, jugadorY)
    mostrar_puntuacion(textoX, textoY)
    pygame.display.update()
