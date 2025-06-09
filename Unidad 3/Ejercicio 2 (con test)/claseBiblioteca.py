class Biblioteca:
    __nombre:str
    __direccion:str
    __telefono:str
    __listaLibros:list

    def __init__(self, nom, dir, tel):
        self.__nombre = nom
        self.__direccion = dir
        self.__telefono = tel
        self.__listaLibros = []
    
    def agregarLibro(self, unLibro):
        self.__listaLibros.append(unLibro)

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getListaLibros(self):
        for libro in self.__listaLibros:
            print(libro)
    
    def __str__(self):
        return f"Nombre: {self.__nombre} - Direccion: {self.__direccion} - Telefono: {self.__telefono}"
    
    def eliminarLibro(self, xlibro):
        i = 0
        encontrado = False

        while i<len(self.__listaLibros) and not encontrado:
            if xlibro == self.__listaLibros[i].getTitulo():
                del self.__listaLibros[i]
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            print("Libro eliminado correctamente")
        else:
            raise IndexError("Libro no encontrado.")
        
    def buscarLibro(self, lib):
        i = 0
        encontrado = False
        aux = None

        while i<len(self.__listaLibros) and not encontrado:
            if lib == self.__listaLibros[i].getTitulo():
                aux = i
                encontrado = True
            else:
                i+= 1
        return aux
    
    def listarLibros(self):
        for libro in self.__listaLibros:
            print(libro)