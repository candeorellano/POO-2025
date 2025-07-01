class Inscripcion:
    __dni:str
    __apellidoYNombre:str
    __idCurso:str
    __diasAsistencia:int
    __notaFinal:int

    def __init__(self, dni, ayn, idc, diasAsis, notaF):
        self.__dni = dni
        self.__apellidoYNombre = ayn
        self.__idCurso = idc
        self.__diasAsistencia = diasAsis
        self.__notaFinal = notaF

    def getDNI(self):
        return self.__dni
    
    def getApellidoYNombre(self):
        return self.__apellidoYNombre
    
    def getIdCurso(self):
        return self.__idCurso
    
    def getDiasAsistencia(self):
        return self.__diasAsistencia
    
    def getNotaFinal(self):
        return self.__notaFinal
    
    def setDiasAsistencia(self, dias):
        self.__diasAsistencia += dias
    
    def setNotaFinal(self, nota):
        self.__notaFinal = nota
    
    def __str__(self):
        return f"DNI: {self.__dni} - Apellido y Nombre: {self.__apellidoYNombre} - ID Curso: {self.__idCurso} - Dias de asistencia: {self.__diasAsistencia} - Nota final: {self.__notaFinal}"
    
    def __lt__(self, otro):
        return self.getApellidoYNombre() < otro.getApellidoYNombre()