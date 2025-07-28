import datetime

class Programa:
    __nombre:str
    __horaInicio:datetime
    __horaFin:datetime

    def __init__(self, nom, horaInicio, horaFin):
        self.__nombre = nom
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin

    def getNombre(self):
        return self.__nombre

    def getHoraInicio(self):
        return self.__horaInicio
    
    def getHoraFin(self):
        return self.__horaFin
    
    def __str__(self):
        return f"Nombre: {self.getNombre()}, Hora de inicio: {self.getHoraInicio()}, Hora de fin: {self.getHoraFin()}"