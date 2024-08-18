import pygame

negro = (4,4,4)
blanco = (255,255,255)

pygame.init()

dimenciones  = [600,600]
ventana = pygame.display.set_mode(dimenciones)
pygame.display.set_captiom("TABLERO DE JUEGO")

Tablero = False
ancho = int(dimenciones[0] / 8)
alto = int(dimenciones[1]/ 8)

while Tablero is False:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Tablero = True
    ventana.fill(blanco)
    color = 0 

for i in range(0,dimenciones[0], ancho):
    if i in range (0,dimenciones[1], alto):
        pygame.draw.rect(ventana, negro [i, j, ancho, alto], 0)
    else:
        pygame.draw.rect(ventana, blanco [i, j, ancho, alto], 0)
    color +- 1
color +- 1

pygame.display.flip()
