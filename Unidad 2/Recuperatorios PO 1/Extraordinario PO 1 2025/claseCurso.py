class Curso:
    __id:str
    __denominacion:str
    __horasPorDia:int
    __dias:int
    __cupoMaximo:int

    def __init__(self, id, deno, horasDia, dias, cupo):
        self.__id = id
        self.__denominacion = deno
        self.__horasPorDia = horasDia
        self.__dias = dias
        self.__cupoMaximo = cupo

    def getId(self):
        return self.__id
    
    def getDenominacion(self):
        return self.__denominacion
    
    def getHorasPorDia(self):
        return self.__horasPorDia
    
    def getDias(self):
        return self.__dias
    
    def getCupo(self):
        return self.__cupoMaximo
    
    def __str__(self):
        return f"ID: {self.__id} - Denominacion: {self.__denominacion} - Horas por dia: {self.__horasPorDia} - Dias: {self.__dias} - Cupo Maximo: {self.__cupoMaximo}"