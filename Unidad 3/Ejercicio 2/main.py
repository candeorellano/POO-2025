from gestorBibliotecas import GestorBiblioteca

def menu():
    op=int(input("""MENU DE OPCIONES
                 [1] Agregar libro
                 [2] Eliminar libro
                 [3] Mostrar nombre de la biblioteca en la que se encuentra un libro
                 [4] Listar libros
                 [0] SALIR
                 --> """))
    return op

if __name__=='__main__':
    GB=GestorBiblioteca()
    GB.cargarArchivo()
    op = menu()

    while op != 0:
        if op == 1:
            GB.mostrar()
            nombreBiblio = input("Ingrese el nombre de la biblioteca: ")
            i = GB.buscarBiblioteca(nombreBiblio) #devuelve la posicion en la que se encuentra la biblioteca
            if i is not None:
                print("Se encontro la biblioteca ingresada")
                titulo = input("Ingrese titulo del libro: ")
                autor = input("Ingrese autor del libro: ")
                isbn = input("Ingrese ISBN del libro: ")
                genero = input("Ingrese genero del libro: ")
                GB.agregarLibro(i, titulo, autor, isbn, genero)
                print("Se agrego correctamente el libro a la biblioteca ingresada. ")
                GB.mostrar() #verifica si se agrego el libro a la biblioteca correspondiente
            else:
                print(f"No se encontro la biblioteca '{nombreBiblio}'.")
        elif op == 2:
            nombreBiblio = input("Ingrese nombre de la biblioteca: ")
            i = GB.buscarBiblioteca(nombreBiblio)
            if i is not None:
                print("Se encontro la biblioteca ingresada: ")
                nombreLibro = input("Ingrese nombre del libro: ")
                GB.eliminarLibro(i, nombreLibro)
                GB.mostrar()
                print("Libro eliminado.")
            else:
                print(f"No se encontro la biblioteca '{nombreBiblio}'.")
        elif op == 3:
            nombreLibro = input("Ingrese el nombre del libro: ")
            GB.recorrerBiblioteca(nombreLibro)
        elif op == 4:
            print("Mostrando todos los libros disponibles...")
            GB.mostrar()
        else:
            print("Opcion incorrecta. Intente de nuevo")
        op = menu()
    print("Saliendo...")
    