class Resultado:
    __fecha:str
    __idEquipoLocal:str
    __golesLocal:int
    __idEquipoVisitante:str
    __golesVisitante:int
    __valorInscripcion=45000

    def __init__(self, fecha, idEquipoLocal, golesLocal, idEquipoVisitante, golesVisitante):
        self.__fecha = fecha
        self.__idEquipoLocal = idEquipoLocal
        self.__golesLocal = golesLocal
        self.__idEquipoVisitante = idEquipoVisitante
        self.__golesVisitante = golesVisitante

    def getFecha(self):
        return self.__fecha
    
    def getIdEquipoLocal(self):
        return self.__idEquipoLocal
    
    def getGolesLocal(self):
        return self.__golesLocal
    
    def getIdEquipoVisitante(self):
        return self.__idEquipoVisitante
    
    def getGolesVisitante(self):
        return self.__golesVisitante
    
    def getValorInscripcion(self):
        return self.__valorInscripcion
    
    def __str__(self):
        return f"Fecha: {self.__fecha}, Equipo Local: {self.__idEquipoLocal} ({self.__golesLocal} goles), Equipo Visitante: {self.__idEquipoVisitante} ({self.__golesVisitante} goles)"
