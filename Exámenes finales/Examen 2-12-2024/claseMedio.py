from abc import ABC, abstractmethod

class Medio(ABC):
    __nombre:str
    __audiencia:int

    def __init__(self, nom, aud):
        self.__nombre = nom
        self.__audiencia = aud

    def getNombre(self):
        return self.__nombre
    
    def getAudiencia(self):
        return self.__audiencia
    
    @abstractmethod
    def indiceAudiencia(self):
        pass

    def __str__(self):
        return f"Nombre: {self.getNombre()}, Audiencia: {self.getAudiencia()}, Indice Audiencia: {self.indiceAudiencia()}"
