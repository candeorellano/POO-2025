from gestorPlanes import GestorPlanes

def menu():
    op=int(input("""MENU DE OPCIONES
                [1] Mostrar que tipo de plan se encuentra almacenado en una posicion de la lista de Planes
                [2] Mostrar la cantidad de planes que pertenecen a una cobertura geografica
                [3] Mostrar las companias que tienen una cantidad de canales internacionales mayor a un valor
                [4] Mostrar datos de todos los planes
                [0] SALIR
                Su opcion -->   """))
    return op

if __name__ == "__main__":
    gestor = GestorPlanes()
    gestor.cargarArchivo()
    
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            try:
                pos = int(input("Ingrese la posicion del plan que desea consultar: "))
                gestor.mostrarTipoPlan(pos)
            except IndexError:
                print("Error. Indice fuera de rango")
            except ValueError:
                print("Error. Se esperaba un numero entero")
        elif opcion == 2:
            cob = input("Ingrese la cobertura geografica a consultar: ")
            cantidad = gestor.cantidadPlanesCobertura(cob)
            print(f"La cantidad de planes con cobertura {cob} es: {cantidad}")
        elif opcion == 3:
            try:
                canales = int(input("Ingrese la cantidad de canales internacionales a consultar: "))
                gestor.companiasPorCantidad(canales)
            except ValueError:
                print("Error. Se esperaba un numero entero")
        elif opcion == 4:
            gestor.mostrarPlanes()
        else:
            print("Opcion no valida, intente nuevamente.")
        opcion = menu()
    print("Saliendo del programa...")