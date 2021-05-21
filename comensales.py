import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Cocinero(threading.Thread):
    def __init__(self, num):
        super().__init__()
#       self.name = 'Cocinero'
        self.name = f'Cocinero {num}'

    def run(self):
        global platosDisponibles

        while (True):
            semaforoCocinero.acquire()
            try:
                logging.info('Reponiendo los platos...')
                platosDisponibles = 3
            finally:
                 semaforoPlato.release()   
                

class Comensal(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Comensal {numero}'

    def run(self):
        global platosDisponibles

        semaforoPlato.acquire()
        try:
            # if platosDisponibles == 0:
            while platosDisponibles == 0:
                semaforoCocinero.release()
                semaforoPlato.acquire()
            platosDisponibles -= 1
            logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
        finally:
            semaforoPlato.release()

semaforoPlato = threading.Semaphore(1)
semaforoCocinero = threading.Semaphore(0)

platosDisponibles = 3

# cocinero = Cocinero()
# cocinero.start()
#Cocinero().start()

for i in range(10):
    Comensal(i).start()

for i in range(5):
    Cocinero(i).start() 