class Matricula:
    __fecha:str
    __empleado:object
    __programa:object

    def __init__(self, fecha, emp, prog):
        self.__fecha = fecha
        self.__empleado = emp
        self.__programa = prog
    
    def __str__(self):
        return f"{self.__fecha}, {self.__empleado}, {self.__programa}"
    
    #Getters
    def getFecha(self):
        return self.__fecha
    
    def getEmpleado(self):
        return self.__empleado
    
    def getPrograma(self):
        return self.__programa