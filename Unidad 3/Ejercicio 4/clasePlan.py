from abc import ABC, abstractmethod

class Plan(ABC):
    __nomCompania:str
    __duracion:int
    __cobertura:str
    __precioBase:int

    def __init__(self, comp, dur, cob, pb):
        self.__nomCompania = comp
        self.__duracion = dur
        self.__cobertura = cob
        self.__precioBase = pb
    
    def getCompania(self):
        return self.__nomCompania
    
    def getDuracion(self):
        return self.__duracion
    
    def getCobertura(self):
        return self.__cobertura
    
    def getPrecioBase(self):
        return self.__precioBase
    
    @abstractmethod
    def getImporteFinal(self):
        pass

    def __str__(self):
        return f"Nombre de la compania: {self.__nomCompania}, Duracion: {self.__duracion} meses, Cobertura: {self.__cobertura}, Precio Base: ${self.__precioBase}"