class Habitacion:
    __numeroH:int
    __piso:int
    __tipo:str
    __precioN:float
    __disponible:bool

    def __init__(self, numeroH, piso, tipo, precio, dispo):
        self.__numeroH = numeroH
        self.__piso = piso
        self.__tipo = tipo
        self.__precioN = precio
        self.__disponible = dispo
    
    def __str__(self):
        return f'Numero: {self.__numeroH}, Piso: {self.__piso}, Tipo: {self.__tipo}, PrecioN: {self.__precioN}, Disponible: {self.__disponible}'
    def getNumero(self):
        return self.__numeroH
    def getPiso(self):
        return self.__piso
    def getTipo(self):
        return self.__tipo
    def getPrecio(self):
        return self.__precioN
    def getDisponibilidad(self):
        return self.__disponible
    def setDisponibilidad(self): #invierte el estado del valor disponible
        self.__disponible = not self.__disponible