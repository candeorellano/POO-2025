class NodoPaciente:
    __paciente: None
    __siguiente: None

    def __init__(self, unPaciente):
        self.__paciente = unPaciente
        self.__siguiente = None

    def getPaciente(self):
        return self.__paciente
    
    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, unSiguiente):
        self.__siguiente = unSiguiente
    