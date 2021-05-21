import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

cantVacas = 5

class Vaca(threading.Thread):
    def __init__(self):
        super().__init__()
        self.posicion = 0
        self.velocidad = random.uniform(0.1, 0.9)

#?????
#        semaforoVaca.acquire()

#        try:
#            while self.posicion > inicioPuente:
#                time.sleep (1 - self.velocidad)
#                self.posicion += 1
#                semaforoVaca.release()    
#        finally:
#            semaforoVaca.release()    


    def avanzar(self):
        time.sleep(1-self.velocidad)
        self.posicion += 1
        if self.posicion == inicioPuente:
            semaforoVaca.acquire()
            while self.posicion < (largoPuente+inicioPuente):
                time.sleep(1-self.velocidad)
                self.posicion += 1
            semaforoVaca.release()   

    def dibujar(self):
        print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V'

    def run(self):
        while(True):
            self.avanzar()
#            while self.posicion == inicioPuente:
#                semaforoVaca.acquire()
#                self.avanzar()
#            while self.posicion > largoPuente:
#                semaforoVaca.release()
#            if self.posicion == 50:
#                self.posicion = 0
                
#Se traban(?) las vacas y no sé cómo arreglarlo.                
                    


vacas = []
semaforoVaca = threading.Semaphore(1)
for i in range(cantVacas):
    v = Vaca()
    vacas.append(v)
    v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
    print(' ' * inicioPuente + '=' * largoPuente)

while(True):
    cls()
    print('Apretá Ctrl + C varias veces para salir...')
    print()
    dibujarPuente()
    for v in vacas:
        v.dibujar()
    dibujarPuente()
    time.sleep(0.2)