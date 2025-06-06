from gestorHotel import GestorHotel

def menu():
    op=int(input("""---MENU PRINCIPAL---
              [1] Agregar habitaciones al hotel.
              [2] Reservar una habitacion.
              [3] Liberar una habitacion 
              [4] Dado un tipo de habitacion (sencilla, doble, suite), mostrar numero y piso de las habitaciones de ese tipo.
              [5] Mostrar la cantidad de habitaciones libres por piso.
              [6] Mostrar detalles de habitaciones por tipo. 
                --> """))
    return op
        
if __name__=='__main__':
    GH=GestorHotel()
    GH.cargarArchivo()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            GH.mostrarDatos()
            nombreHotel=input("Ingrese el nombre del hotel: ")
            i = GH.buscarHotel(nombreHotel)
            if i != -1:
                print(f"Se encontro el hotel '{nombreHotel}'")
                numHab=int(input("Indique el numero de habitacion: "))
                piso=int(input("Ingrese el numero de piso: "))
                tipo=input("Indique el tipo de habitacion (sencilla, doble o suite): ")
                precio=float(input("Indique el precio por noche: $"))
                dispo=True #deberia ser True ya que no fue reservada todavia
                GH.agregar_Habitacion(i, numHab, piso, tipo, precio, dispo)
                print("Se agrego correctamente la habitacion al hotel indicado.")
                GH.mostrarDatos() #lista los datos del gestor de los hoteles con sus respectivas habitaciones
            else:
                print(f"No se encontro el hotel '{nombreHotel}'")
        elif opcion == 2:
            GH.mostrarDatos()
            nombreHotel=input("Ingrese el nombre del hotel: ")
            i = GH.buscarHotel(nombreHotel)
            if i != -1:
                print(f"Se encontro el hotel '{nombreHotel}'")
                numero=int(input("Ingrese el numero de habitacion: "))
                GH.reservarHabitacion(i, numero)
                GH.mostrarDatos()
            else:
                print(f"No se encontro el hotel '{nombreHotel}'")
        elif opcion == 3:
            GH.mostrarDatos()
            nombreHotel=input("Ingrese el nombre del hotel: ")
            i = GH.buscarHotel(nombreHotel)
            if i != -1:
                print(f"Se encontro el hotel '{nombreHotel}'")
                numero=int(input("Ingrese el numero de habitacion: "))
                GH.liberarHabitacion(i, numero)
                GH.mostrarDatos()
            else:
                print(f"No se encontro el hotel '{nombreHotel}'")
        elif opcion == 4:
                tipo=input("Indique el tipo de habitacion: ")
                GH.mostrarPorTipo(tipo)
        elif opcion == 5:
                GH.mostrarHabitacionesLibres()
        elif opcion == 6:
            GH.inciso6()
        else:
            print("Opcion incorrecta. Intente de nuevo")
        opcion = menu()