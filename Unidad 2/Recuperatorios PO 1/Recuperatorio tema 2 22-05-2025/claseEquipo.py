class Equipo:
    __id:str
    __denominacion:str
    __presidente:str
    __puntos:int
    __golesAFavor:int
    __golesEnContra:int
    __diferenciaGoles:int

    def __init__(self, id, deno, presidente, puntos, golesAFavor, golesEnContra):
        self.__id = id
        self.__denominacion = deno
        self.__presidente = presidente
        self.__puntos = puntos
        self.__golesAFavor = golesAFavor
        self.__golesEnContra = golesEnContra
        self.__diferenciaGoles = golesAFavor - golesEnContra

    #Getters
    def getId(self):
        return self.__id
    
    def getDenominacion(self):
        return self.__denominacion
    
    def getPresidente(self):
        return self.__presidente
    
    def getPuntos(self):
        return self.__puntos
    
    def setPuntos(self, puntos):
        self.__puntos += puntos #suma los puntos

    def getGolesAFavor(self):
        return self.__golesAFavor
    
    def getGolesEnContra(self):
        return self.__golesEnContra
    
    def getDiferenciaGoles(self):
        return self.__diferenciaGoles
    
    #Setters
    def setGolesAFavor(self, goles):
        self.__golesAFavor += goles

    def setGolesEnContra(self, goles):
        self.__golesEnContra += goles

    def setDiferenciaGoles(self, diferencia):
        self.__diferenciaGoles += diferencia

    def __str__(self):
        return f"ID: {self.__id}, Denominación: {self.__denominacion}, Presidente: {self.__presidente}, Puntos: {self.__puntos}, Goles a Favor: {self.__golesAFavor}, Goles en Contra: {self.__golesEnContra}, Diferencia de Goles: {self.__diferenciaGoles}"
    
    def __gt__(self, otro):
        retorno = None

        if self.__puntos != otro.__puntos:
            retorno = self.__puntos > otro.__puntos
        elif self.__diferenciaGoles != otro.__diferenciaGoles:
            retorno = self.__diferenciaGoles > otro.__diferenciaGoles
        else:
            retorno = self.__golesAFavor > otro.__golesAFavor
        
        return retorno
