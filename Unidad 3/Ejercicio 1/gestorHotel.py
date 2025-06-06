from claseHotel import Hotel
import csv

class GestorHotel:
    __listaHoteles:list

    def __init__(self):
        self.__listaHoteles = []

    def agregarHotel(self, unHotel):
        self.__listaHoteles.append(unHotel)

    def cargarArchivo(self):
        i = -1
        with open("Hoteles.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv, delimiter=';')

            for fila in reader:
                if len(fila) == 3:
                    # Línea de datos del hotel
                    self.agregarHotel(Hotel(fila[0], fila[1], fila[2]))
                    i += 1
                else:
                    # Línea de datos de habitación
                    nro = int(fila[0])
                    piso = int(fila[1])
                    tipo = fila[2]
                    precio = float(fila[3])

                    # Manejo correcto de la disponibilidad
                    if fila[4].strip().lower() == "true":
                        disponibilidad = True
                    else:
                        disponibilidad = False

                    self.__listaHoteles[i].agregarHabitacion(nro, piso, tipo, precio, disponibilidad)
            archivo_csv.close()

    def buscarHotel(self, nombre):
        i = 0
        encontrado = False

        while i < len(self.__listaHoteles) and not encontrado:
            if nombre.strip().lower() == self.__listaHoteles[i].getNombre().strip().lower():
                encontrado = True
            else:
                i += 1

        if encontrado:
            return i
        else:
            return -1

    
    def agregar_Habitacion(self, i, num, piso, tipo, precio, dispo):
       self.__listaHoteles[i].agregarHabitacion(num, piso, tipo, precio, dispo)
    
    def reservarHabitacion(self, i, num): #trae el indice del hotel
        iHab = self.__listaHoteles[i].buscaHabPorNum(num) #devuelve el indice de la habitacion en el hotel i
        disponibilidad = self.__listaHoteles[i].getDisponibilidad(iHab) #obtiene la disponibilidad de esa habitacion

        if disponibilidad == True:
            self.__listaHoteles[i].setDisponibilidad(iHab)
            print(f"La habitacion {num} fue reservada exitosamente.")
        else:
            print(f"La habitacion {num} esta reservada.")

    def liberarHabitacion(self, i, num):
        iHab = self.__listaHoteles[i].buscaHabPorNum(num) #devuelve el indice de la habitacion en el hotel i
        disponibilidad = self.__listaHoteles[i].getDisponibilidad(iHab) #obtiene la disponibilidad de esa habitacion

        if disponibilidad == False:
            self.__listaHoteles[i].setDisponibilidad(iHab)
            print(f"La habitacion {num} fue liberada exitosamente.")
        else:
            print(f"La habitacion {num} ya esta liberada.")

    def mostrarPorTipo(self, tipo):
        for hotel in self.__listaHoteles:
            nombre = hotel.getNombre()
            print(f"Hotel {nombre}")
            hotel.mostrarTipo(tipo)

    def mostrarHabitacionesLibres(self):
        for hotel in self.__listaHoteles:
            nombre = hotel.getNombre()
            print(f"Hotel {nombre}")
            cantidad = hotel.contarHabLibres()
            print(f"Cantidad de habitaciones libres del hotel: {cantidad}")
    
    def inciso6(self):
        for hotel in self.__listaHoteles:
            nombre = hotel.getNombre()
            print(f"Hotel {nombre}")
            hotel.listarPorTipo()
    
    def mostrarDatos(self):
        for hotel in self.__listaHoteles:
            print(f"Hotel: {hotel.getNombre()}")
            hotel.mostrarHabitaciones()