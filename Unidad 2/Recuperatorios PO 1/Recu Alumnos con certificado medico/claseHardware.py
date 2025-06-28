class Hardware:
    __id:str
    __descripcion:str
    __ubicacion:str

    def __init__(self, id, desc, ubic):
        self.__id = id
        self.__descripcion = desc
        self.__ubicacion = ubic
    
    def getId(self):
        return self.__id
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getUbicacion(self):
        return self.__ubicacion
    
    def __str__(self):
        return f"ID: {self.__id}, Descripcion: {self.__descripcion}, Ubicacion: {self.__ubicacion}"