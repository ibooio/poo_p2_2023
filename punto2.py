from threading import Thread
import random, time
from abc import abstractmethod

class Transformador(Thread):
    def __init__(self, nombre, min_sleep, max_sleep, numero):
        super().__init__()
        self.__nombre = nombre
        self.__min_sleep = min_sleep
        self.__max_sleep = max_sleep
        self._numero = numero

    def run (self):
        tiempo = random.randint(self.__min_sleep,self.__max_sleep)
        time.sleep(tiempo)
        resultado = self.transformar()
        print(f"{self.__nombre} : {self._numero} => {resultado}")
    
    @abstractmethod
    def transformar (self): 
        pass

class TransformadorUno (Transformador):    
    def __init__(self, numero):
        super().__init__('Transformador 1', 2, 7, numero)
    
    def transformar(self):
         resultado = self._numero
         for i in range(1,11):
            resultado *= 10
         return resultado

class TransformadorDos (Transformador):    
    def __init__(self, numero):
        super().__init__('Transformador 2', 3, 5, numero)
    
    def transformar(self):
         resultado = self._numero
         for i in range(1,11):
            resultado /= 10
         return resultado
    
class TransformadorTres (Transformador):    
    def __init__(self, numero):
        super().__init__('Transformador 3', 1, 10, numero)
    
    def transformar(self):
         return self._numero + 1000

if __name__ == '__main__':    
    for i in range(1,4):
        numero = random.randint(1,10)
        transformador_uno = TransformadorUno(numero)
        transformador_uno.start()
        
        transformador_dos = TransformadorDos(numero)
        transformador_dos.start()
        
        transformador_tres = TransformadorTres(numero)
        transformador_tres.start()