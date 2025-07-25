from claseMedio import Medio

class NodoMedio:
    __medio: Medio
    __siguiente: object

    def __init__(self, medio):
        self.__medio = medio
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getMedio(self):
        return self.__medio
    