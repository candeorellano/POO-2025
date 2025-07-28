from claseMedio import Medio

class Prensa(Medio):
    __periodicidad: str
    __secciones:int

    def __init__(self, nom, aud, peri, sec):
        super().__init__(nom, aud)
        self.__periodicidad = peri
        self.__secciones = sec

    def getPeriodicidad(self):
        return self.__periodicidad
    
    def getSecciones(self):
        return self.__secciones
    
    def indiceAudiencia(self):
        if self.getSecciones() > 0 and self.getPeriodicidad() == "mensual":
            indice = self.getAudiencia() / self.getSecciones()
        elif self.getSecciones() > 0 and self.getPeriodicidad() == "semanal":
            indice = self.getAudiencia() / (self.getSecciones() * 4)
        else:
            indice = 0
        return indice
    
    def __str__(self):
        return f"{super().__str__()}, Periodicidad: {self.getPeriodicidad()}, Cantidad de secciones: {self.getSecciones()}"