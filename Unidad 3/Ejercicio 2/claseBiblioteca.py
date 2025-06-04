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

    def agregar_Libro(self, libro):
        self.__listaLibros.append(libro)
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getListaLibros(self):
        return self.__listaLibros

    def __str__(self):
        return f"Nombre: {self.__nombre} - Direccion: {self.__direccion} - Telefono: {self.__telefono}"
    
    def buscarLibro(self, nombre):
        encontrado = False
        i = 0

        while i<len(self.__listaLibros)  and not encontrado:
            if self.__listaLibros[i].getTitulo() == nombre:
                del self.__listaLibros[i]
                encontrado = True
            else:
                i+=1
    
    def buscarLibro2(self, nombre):
        encontrado = False
        i = 0
        aux = None

        while i<len(self.__listaLibros) and not encontrado:
            if nombre == self.__listaLibros[i].getTitulo():
                encontrado = True
                autor = self.__listaLibros[i].getAutor()
                genero = self.__listaLibros[i].getGenero()
                print(f"Autor: {autor} - Genero: {genero}")
                aux = i
            else:
                i += 1
        return aux
    
    def mostrarLibros(self):
        for libro in self.__listaLibros:
            print(libro)