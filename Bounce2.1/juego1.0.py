# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:11:01 2017

@author: Luis
"""

import pygame,sys
from pygame.locals import *
from random import randint  # crear numeros aleatorios

ancho = 800
alto = 600
posX = 0
posY = 520

Blanco = (255,255,255)
Negro = (0,0,0,0)
Rojo = (178,34,4)

class Moneda(pygame.sprite.Sprite): # heredar de pygame.Sprite..
    """"Clase para la nave"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #usar sprite en la imagen
        self.moneda = pygame.image.load("Imagenes/moneda.png")
        self.moneda = pygame.transform.scale(self.moneda, (35,35))
        self.rect = self.moneda.get_rect()

        
        
    def dibujar(self, superficie, x, y):
        self.rect.centerx = x
        self.rect.centery = y
        
        superficie.blit(self.moneda, self.rect)

    def nodibujar(self, superficie, x, y):
        
        superficie.blit(self.moneda, self.rect)

class Bola(Moneda): # heredar de pygame.Sprite..
    """"Clase para la nave"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #usar sprite en la imagen
        self.bola = pygame.image.load("Imagenes/bola.png")
        self.bola = pygame.transform.scale(self.bola, (35,35))
        self.rect = self.bola.get_rect()

        self.velocidad = 40
        
        self.change_x = 0
        self.change_y = 0
        self.vida = True

        
    def actualizar(self,moneda):
        if pygame.sprite.collide_rect(self,moneda):
            print("colision")

            

    
            
        
    def dibujar(self, superficie):
        superficie.blit(self.bola, self.rect)
        
    def cambiovelocidad(self,x,y):
        """Cambiamos la velocidad del protagonista"""
        self.change_x += x
        self.change_y += y
        
    # LIMITES DE LA PANTALLA 
    def movimiento(self):
        if self.vida == True:
            
            if self.rect.left<=0:
                self.rect.left =5
            elif self.rect.right>=800:
                self.rect.right = 800
            elif self.rect.top >=560:
                self.rect.top = 560
            elif self.rect.bottom <=30:
                self.rect.bottom = 30

            
    # Encontramos una posición nueva para el protagonista
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y


         

pygame.init()
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Juego")
imagenFondo = pygame.image.load("Imagenes/fondo1.jpg")
imagenFondo = pygame.transform.scale(imagenFondo, (800,600))

jugador = Bola()
monedas = Moneda()
listade_todoslos_sprites = pygame.sprite.Group()
listade_todoslos_sprites.add(jugador)

#moneda = pygame.image.load("Imagenes/moneda.png") 
#moneda = pygame.transform.scale(moneda, (35,35))

#ventana.blit(moneda,(225,500))

s1 = pygame.Surface([300,70])
s2 = pygame.Surface([310,80])
s1.fill(Negro)
s2.fill(Rojo)



#velocidad = 5 # velocidad de 5 pixeles
enJuego = True

reloj = pygame.time.Clock()

puntuacion = pygame.mixer.music.load("Sonido/intro.mp3")
pygame.mixer.music.play(2)    

          
while True:
    #sound.play()
    jugador.movimiento()
    for evento in pygame.event.get(): # regresa una lista de eventos
        if evento.type == QUIT: # si se presiona x se cierra la venta
                pygame.quit()
                sys.exit()
        if enJuego == True:
                if evento.type == pygame.KEYDOWN: # SI ALGUNA TECLA FUE PRESIONADA
                    if evento.key == pygame.K_LEFT:
                        jugador.cambiovelocidad(-3,0)
                    elif evento.key == pygame.K_RIGHT:
                        jugador.cambiovelocidad(3,0)
                    elif evento.key == pygame.K_UP: 
                        jugador.cambiovelocidad(0,-3)
                    elif evento.key == pygame.K_DOWN:
                        jugador.cambiovelocidad(0,3)
                elif evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT:
                        jugador.cambiovelocidad(3,0)
                    elif evento.key == pygame.K_RIGHT:
                        jugador.cambiovelocidad(-3,0)
                    elif evento.key == pygame.K_UP:
                        jugador.cambiovelocidad(0,3)
                    elif evento.key == pygame.K_DOWN:
                        jugador.cambiovelocidad(0,-3)
    

    # Reseteamos la velocidad cuando la tecla es hacia arriba      
    # Esto mueve al bloque protagonista según la velocidad actual
    listade_todoslos_sprites.update()
    

    # Pausa
    reloj.tick(60)
        
    
    ventana.blit(imagenFondo, (0,0))

    ventana.blit(s2, (0,150))
    ventana.blit(s1, (5,155))

    jugador.actualizar(monedas)
    monedas.dibujar(ventana, 100,500)
    
    jugador.dibujar(ventana)
    
    #ventana.blit(moneda,(450,500))
    #ventana.blit(moneda,(500,500))
    #ventana.blit(moneda,(550,500))

    
    pygame.display.update()