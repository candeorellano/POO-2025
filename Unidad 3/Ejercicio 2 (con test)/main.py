from claseBiblioteca import Biblioteca
from claseLibro import Libro
from gestorBibliotecas import GestorBibliotecas

def test():
    GB = GestorBibliotecas()
    libro1=Libro('El Principito','Antoine de Saint-Exupéry','9780156012195','Fábula')
    libro2=Libro('Rayuela','Julio Cortázar','9788437600949','Ficción')
    libro3=Libro('Don Quijote de la Mancha','Miguel de Cervantes','9788491050257','Clásico')
    biblioteca1=Biblioteca('Biblioteca Central','Av. Libertad 456','0351-4567890')
    biblioteca1.agregarLibro(libro1)
    biblioteca2=Biblioteca('Biblioteca Popular','San Martín 123','0341-1234567')
    biblioteca2.agregarLibro(libro2)
    biblioteca2.agregarLibro(libro3)

    GB.agregarBiblioteca(biblioteca1)
    GB.agregarBiblioteca(biblioteca2)

def menu():
    try:
        op=int(input("""MENU DE OPCIONES:
                 [1] Agregar libro
                 [2] Eliminar libro
                 [3] Mostrar nombre de la biblioteca en la que se encuentra un libro
                 [4] Listar libros
                 [0] SALIR
                 --> """))
    except ValueError:
        print("Error. Se esperaba un numero entero.")
    return op

if __name__=='__main__':
    gb = GestorBibliotecas()
    #test() #carga los libros y bibliotecas
    libro1=Libro('El Principito','Antoine de Saint-Exupéry','9780156012195','Fábula')
    libro2=Libro('Rayuela','Julio Cortázar','9788437600949','Ficción')
    libro3=Libro('Don Quijote de la Mancha','Miguel de Cervantes','9788491050257','Clásico')
    biblioteca1=Biblioteca('Biblioteca Central','Av. Libertad 456','0351-4567890')
    biblioteca1.agregarLibro(libro1)
    biblioteca2=Biblioteca('Biblioteca Popular','San Martín 123','0341-1234567')
    biblioteca2.agregarLibro(libro2)
    biblioteca2.agregarLibro(libro3)

    gb.agregarBiblioteca(biblioteca1)
    gb.agregarBiblioteca(biblioteca2)

    opcion = menu()

    while opcion != 0:
        try:
            if opcion == 1:
                nombre = input("Ingrese el nombre de la biblioteca a la cual desea agregarle un libro: ")
                i = gb.buscaBiblio(nombre)
                tit = input("Indique el titulo del libro: ")
                aut = input("Indique el autor del libro: ")
                isbn = input("Ingrese el ISBN del libro: ")
                gen = input("Indique genero del libro: ")
                unLibro = Libro(tit, aut, isbn, gen)
                gb.addLibro(i, unLibro)
            elif opcion == 2:
                nombre = input("Ingrese el nombre de la biblioteca a la cual desea eliminarle un libro: ")
                i = gb.buscaBiblio(nombre)
                lib = input("Ingrese el nombre del libro que desea eliminar: ")
                gb.eliminaLibro(i, lib)
            elif opcion == 3:
                librito = input("Ingrese el nombre del libro: ")
                gb.mostrarBiblio(librito)
            elif opcion == 4:
                gb.listar()
            else:
                print("Opcion incorrecta. Intente de nuevo")
        except ValueError:
            print("Error. Se esperaba un numero entero.")
        opcion = menu()