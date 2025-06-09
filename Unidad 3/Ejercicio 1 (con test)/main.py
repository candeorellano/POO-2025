from gestorHoteles import GestorHoteles
from claseHotel import Hotel

def menu():
    try:
        op=int(input("""---MENU PRINCIPAL---
                [1] Agregar habitaciones al hotel.
                [2] Reservar una habitacion.
                [3] Liberar una habitacion 
                [4] Dado un tipo de habitacion (sencilla, doble, suite), mostrar numero y piso de las habitaciones de ese tipo.
                [5] Mostrar la cantidad de habitaciones libres por piso.
                [6] Mostrar detalles de habitaciones por tipo. 
                    --> """))
        return op
    except ValueError:
        print("Error. Se esperaba un numero entero")

if __name__=='__main__':
    gh = GestorHoteles()

    #carga
    hotel1 = Hotel('Central','Avenida Ignacio de la Roza 123','2644200584')
    hotel1.agregarHabitacion(102,1,'sencilla',5000.0,True)
    hotel1.agregarHabitacion(101,1,'sencilla',5000.0,False)
    gh.agregarHotel(hotel1) #despues de agregar las habitaciones, agrego el hotel

    hotel2 = Hotel('Paraiso Tropical','Avenida Costera 1234','0341698631')
    hotel2.agregarHabitacion(202,2,'doble',8000.0,True)
    hotel2.agregarHabitacion(301,3,'suite',10000.0,False)
    gh.agregarHotel(hotel2)

    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            nombre = input("Ingrese el nombre del hotel al que desea agregarle una habitacion: ")
            try:
                i = gh.buscarHotel(nombre)
                numHab=int(input("Ingrese el numero de habitacion: "))
                p=int(input("Ingrese el piso de la habitacion: "))
                t=input("Indique el tipo de habitacion (sencilla, doble, suite): ")
                precio=float(input("Indique el precio de la habitacion: "))
                dispo=True
                gh.agregarHab(i, numHab,p,t,precio,dispo)
            except IndexError as e:
                print(e)
        elif opcion == 2:
            nombre = input("Ingrese el nombre del hotel al que desea reservar una habitacion: ")
            try:
                i = gh.buscarHotel(nombre)
                num=int(input("Ingrese el numero de habitacion: "))
                gh.reservaHab(i, num)
            except IndexError as e:
                print(e)
        elif opcion == 3:
            nombre = input("Ingrese el nombre del hotel al que desea liberar una habitacion: ")
            try:
                i = gh.buscarHotel(nombre)
                num=int(input("Ingrese el numero de habitacion: "))
                gh.liberaHab(i, num)
            except IndexError as e:
                print(e)
        elif opcion == 4:
            tipo = input("Indique el tipo de habitacion: ")
            gh.mostrarHab(tipo)
        elif opcion == 5:
            gh.mostrarHabLibres()
        elif opcion == 6:
            gh.mostrarPorTipo()
        else:
            print("Opcion incorrecta. Intente de nuevo")
        opcion = menu()
    print("Saliendo...")