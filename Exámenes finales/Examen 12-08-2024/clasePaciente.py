class Paciente:
    __nombre:str
    __apellido:str
    __email:str
    __telefono:str
    __consulta = 15000

    def __init__(self, nom, apell, email, tel):
        self.__nombre = nom
        self.__apellido = apell
        self.__email = email
        self.__telefono = tel

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEmail(self):
        return self.__email
    
    def getTelefono(self):
        return self.__telefono
    
    @classmethod
    def getConsulta(cls):
        return cls.__consulta
    
    def getImporte(self):
        return self.getConsulta()
    
    @classmethod
    def setConsulta(cls, nuevoImporte):
        cls.__consulta = nuevoImporte
    
    def __str__(self):
        return f"Nombre: {self.getNombre()}, Apellido: {self.getApellido()}, Email: {self.getEmail()}, Telefono: {self.getTelefono()}, Importe a cobrar: ${self.getImporte()}"