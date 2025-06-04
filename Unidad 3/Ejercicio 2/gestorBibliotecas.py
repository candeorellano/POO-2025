from claseBiblioteca import Biblioteca
from claseLibro import Libro
import csv

class GestorBiblioteca:
    __listaBiblioteca:list

    def __init__(self):
        self.__listaBiblioteca = []

    def agregarBiblioteca(self, unaBiblioteca):
        self.__listaBiblioteca.append(unaBiblioteca)

    def cargarArchivo(self):
        i=-1
        with open("Biblioteca.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv, delimiter=';')

            for fila in reader:
                if len(fila)==3:
                    self.agregarBiblioteca(Biblioteca(fila[0], fila[1], fila[2]))
                    i+=1
                else:
                    titulo=fila[0]
                    autor=fila[1]
                    isbn=fila[2]
                    genero=fila[3]
                    unLibro=Libro(titulo, autor, isbn, genero)
                    self.__listaBiblioteca[i].agregar_Libro(unLibro)
            archivo_csv.close()
    
    def buscarBiblioteca(self, nombre): #busca una biblioteca por el nombre y si la encuentra, devuelve la posicion de la biblioteca
        i=0
        encontrado=False

        while i<len(self.__listaBiblioteca) and not encontrado:
            if nombre == self.__listaBiblioteca[i].getNombre():
                encontrado = True
            else:
                i += 1
        return i
    
    def agregarLibro(self, i, titulo, autor, isbn, genero):
        libro = Libro(titulo, autor, isbn, genero)
        self.__listaBiblioteca[i].agregar_Libro(libro)

    def eliminarLibro(self, i, nomLibro):
        self.__listaBiblioteca[i].buscarLibro(nomLibro)

    def recorrerBiblioteca(self, nomLibro): #recorre todas las bibliotecas porque el libro puede estar en una, varias o todas
        encontrado = False
        for biblioteca in self.__listaBiblioteca:
            i = biblioteca.buscarLibro2(nomLibro)
            if i is not None:
                print(f"Biblioteca: {biblioteca.getNombre()}")
                encontrado = True
        if not encontrado:
            print("El libro ingresado no fue encontrado en ninguna biblioteca")

    def mostrar(self):
        for biblioteca in self.__listaBiblioteca:
            print(f"{biblioteca.getNombre()}")
            biblioteca.mostrarLibros()
