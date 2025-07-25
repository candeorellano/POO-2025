from gestorMedios import GestorMedios

def menu():
    op = int(input("""MENU DE OPCIONES:
                   [1] Insertar medio a la coleccion en una determinada posicion
                   [2] Agregar medio a la coleccion
                   [3] Listar medios
                   [4] Mostrar el nombre del canal en el que se transmite un programa de television y su
                    horario de transmision
                   [5] Listar la programacion de una emisora de radio: nombre y horario de cada programa
                   [6] Indicar la cantidad de diarios y revistas almacenados en la coleccion
                   [0] SALIR
                    Elija una opcion: """))
    return op

if __name__ == '__main__':
    gm = GestorMedios()
    gm.leeArchivos()

    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            try:
                pos = int(input("Ingrese la posicion donde desea insertar el medio: "))
                gm.inciso1(pos)
                gm.listarMedios()
            except IndexError:
                print("Error: Posición fuera de rango.")
            except ValueError:
                print("Error: Debe ingresar un número entero para la posición.")
        elif opcion == 2:
            try:
                gm.inciso2()
                gm.listarMedios()
            except TypeError:
                print("Error: El medio debe ser una instancia de la clase 'T', 'R' o 'P'.")
        elif opcion == 3:
            gm.listarMedios()
        elif opcion == 4:
            prog = input("Ingrese el nombre del programa de television: ")
            gm.mostrarCanalYHorario(prog)
        elif opcion == 5:
            nombreEmisora = input("Ingrese el nombre de la emisora de radio: ")
            gm.listarProgramacionEmisora(nombreEmisora)
        elif opcion == 6:
            gm.contarDiariosYRevistas()
        else:
            print("Opcion no valida. Intente nuevamente.")
        
        opcion = menu()
    print("Saliendo del programa...")