class Programa:
    __nombre:str
    __horaInicio:str
    __horaFin:str

    def __init__(self, nom, inicio, fin):
        self.__nombre = nom
        self.__horaInicio = inicio
        self.__horaFin = fin

    def getNombre(self):
        return self.__nombre
    
    def getHoraInicio(self):
        return self.__horaInicio
    
    def getHoraFin(self):
        return self.__horaFin
    
    def __str__(self):
        return f"Programa: {self.__nombre}, Inicio: {self.__horaInicio}, Fin: {self.__horaFin}"