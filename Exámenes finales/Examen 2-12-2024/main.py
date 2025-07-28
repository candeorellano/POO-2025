from gestorMedios import GestorMedios

def menu():
    op = int(input("""MENU DE OPCIONES
                   [1] Agregar medios a la coleccion
                   [2] Mostrar el nombre del medio de comunicacion de un programa de radio, la frecuencia y el horario de transmision
                   [3] Indicar para cada medio el nombre, audiencia y el indice de audiencia
                   [0] SALIR
                   Ingrese una opcion: """))
    return op

if __name__=='__main__':
    gm = GestorMedios()
    
    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            gm.leeArchivo()
        elif opcion == 2:
            try:
                prog = input("Ingrese el nombre del programa de radio: ")
                gm.mostrarDatosPrograma(prog)
            except Exception:
                print(f"Error: Programa no encontrado en ninguna radio")
        elif opcion == 3:
            gm.mostrarMedios()
        else:
            print("Opcion no valida. Intente nuevamente.")
        opcion = menu()
    print("Saliendo del programa...")
