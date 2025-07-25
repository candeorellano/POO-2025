from claseMedio import Medio

class Prensa(Medio):
    __tipoPublicacion:str
    __periodicidad:str

    def __init__(self, nom, aud, tipoPub, periodicidad):
        super().__init__(nom, aud)
        self.__tipoPublicacion = tipoPub
        self.__periodicidad = periodicidad

    def getTipoPublicacion(self):
        return self.__tipoPublicacion
    
    def getPeriodicidad(self):
        return self.__periodicidad

    def __str__(self):
        return f"{super().__str__()}, Tipo de Publicación: {self.__tipoPublicacion}, Periodicidad: {self.__periodicidad}"