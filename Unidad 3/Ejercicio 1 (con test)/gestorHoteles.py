from claseHotel import Hotel

class GestorHoteles():
    __listaHoteles:list

    def __init__(self):
        self.__listaHoteles = []

    def agregarHotel(self, unHotel):
        self.__listaHoteles.append(unHotel)
    
    def buscarHotel(self, nom):
        i = 0
        encontrado = False
        aux = None

        while i<len(self.__listaHoteles) and not encontrado:
            if nom == self.__listaHoteles[i].getNombre():
                encontrado = True
                aux = i
            else:
                i+=1
        
        if encontrado:
            return aux
        else:
            raise IndexError("El hotel no se encuentra en la lista")
    
    def agregarHab(self, i, num, piso, tipo, precio, disp):
        self.__listaHoteles[i].agregarHabitacion(num,piso,tipo,precio,disp)

    def reservaHab(self, i, hab):
        iHab = self.__listaHoteles[i].buscaHabPorNum(hab)
        dispo = self.__listaHoteles[i].getDisponibilidad(iHab)
        if dispo == True:
            self.__listaHoteles[i].reservarHabitacion(iHab)
            print("Habitacion reservada correctamente")
        else:
            print(f"La habitacion {hab} ya fue reservada.")
    
    def liberaHab(self, i, hab):
        iHab = self.__listaHoteles[i].buscaHabPorNum(hab)
        dispo = self.__listaHoteles[i].getDisponibilidad(iHab)
        if dispo == False:
            self.__listaHoteles[i].liberarHabitacion(iHab)
            print("Habitacion liberada correctamente")
        else:
            print(f"La habitacion {hab} no esta reservada")
        
    def mostrarHab(self, tipo):
        for hotel in self.__listaHoteles:
            print(f"Hotel: {hotel.getNombre()}")
            hotel.muestraHabPorTipo(tipo)
    
    def mostrarHabLibres(self):
        for hotel in self.__listaHoteles:
            print(f"Hotel: {hotel.getNombre()}")
            cant = hotel.contarHabLibres()
            print(f"Cantidad de habitaciones libres del hotel: {cant}")
    
    def mostrarPorTipo(self):
        for hotel in self.__listaHoteles:
            print(f"Hotel: {hotel.getNombre()}")
            hotel.mostrarDetalles()
    
    def mostrarDatos(self):
        for hotel in self.__listaHoteles:
            print(f"Hotel: {hotel.getNombre()}")
            hotel.mostrarHabitaciones()