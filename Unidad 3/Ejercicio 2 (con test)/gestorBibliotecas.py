class GestorBibliotecas:
    __listaBibliotecas:list

    def __init__(self):
        self.__listaBibliotecas = []
    
    def agregarBiblioteca(self, unaBiblo):
        self.__listaBibliotecas.append(unaBiblo)
    
    def buscaBiblio(self, nombre):
        i = 0
        aux = None
        encontrado = False

        while i<len(self.__listaBibliotecas) and not encontrado:
            if nombre == self.__listaBibliotecas[i].getNombre():
                encontrado = True
                aux = i
            else:
                i +=1
        
        if encontrado:
            return aux
        else:
            raise IndexError("Biblioteca no encontrada")
        
    def addLibro(self, pos, libro):
        self.__listaBibliotecas[pos].agregarLibro(libro)
    
    def eliminaLibro(self, pos, xlibro):
        self.__listaBibliotecas[pos].eliminarLibro(xlibro)

    def mostrarBiblio(self, librito):
        encontrado = False
        for biblioteca in self.__listaBibliotecas:
            i = biblioteca.buscarLibro(librito)
            if i is not None:
                print(f"Biblioteca: {biblioteca.getNombre()}")
                encontrado = True
        
        if not encontrado:
            print("El libro no fue encontrado en ninguna biblioteca")

    def listar(self):
        for biblioteca in self.__listaBibliotecas:
            print(f"Biblioteca: {biblioteca.getNombre()}")
            biblioteca.listarLibros()