class Empleado:
    __NomyApell:str
    __id:int
    __puesto:str

    def __init__(self, nya, id, puesto):
        self.__NomyApell = nya
        self.__id = id
        self.__puesto = puesto

    def __str__(self):
        return f"Nombre y Apellido: {self.__NomyApell}, ID: {self.__id}, Puesto: {self.__puesto}"
    
    #Getters
    def getNyA(self):
        return self.__NomyApell
    def getId(self):
        return self.__id
    def getPuesto(self):
        return self.__puesto
