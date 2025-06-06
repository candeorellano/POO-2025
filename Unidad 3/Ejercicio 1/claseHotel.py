from claseHabitacion import Habitacion

class Hotel:
    __nombre: str
    __direccion: str
    __telefono: str
    __lista_habitaciones: list
    
    
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__lista_habitaciones = []
    
    def agregarHabitacion(self, nro, piso, tipo, precio, dispo):
        unaHabitacion = Habitacion(nro, piso, tipo, precio, dispo)
        self.__lista_habitaciones.append(unaHabitacion)

    #Getters
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getListaHab(self):
        return self.__lista_habitaciones
    
    def __str__(self):
        print(f"{self.__nombre} {self.__direccion} {self.__telefono} {self.__telefono} {self.__lista_habitaciones}")
        print(f"LISTA DE HABITACIONES:")
        for habitacion in self.__lista_habitaciones:
            print(f"{habitacion}")

    def buscaHabPorNum(self, xnum):
        i=0
        encontrado=False

        while i<len(self.__lista_habitaciones) and not encontrado:
            if xnum == self.__lista_habitaciones[i].getNumero():
                encontrado = True
            else:
                i += 1
        return i
    
    def getDisponibilidad(self, iHab):
        disponibilidad = self.__lista_habitaciones[iHab].getDisponible()
        return disponibilidad

    def setDisponibilidad(self, iHab):
        self.__lista_habitaciones[iHab].setDisponible()

    def mostrarTipo(self, xtipo):
        for habitacion in self.__lista_habitaciones:
            if xtipo == habitacion.getTipo():
                numero = habitacion.getNumero()
                piso = habitacion.getPiso()
                print(f"Habitacion de tipo {xtipo} N°: {numero} - Piso: {piso}")

    def contarHabLibres(self):
        cont=0
        for habitacion in self.__lista_habitaciones:
            if habitacion.getDisponible() == True:
                cont+=1
        return cont
    
    def tiposHabitacion(self):
        tipos = []
        for habitacion in self.__lista_habitaciones:
            tipo= habitacion.getTipo()
            if tipo not in tipos:
                tipos.append(tipo)
        return tipos
    
    def listarPorTipo(self):
        tiposHab = self.tiposHabitacion()
        
        for tipo in tiposHab:
            print(f"Tipo de habitacion: {tipo}")
            print("Numero   Piso    Precio por Noche    Disponibilidad")
            for habitacion in self.__lista_habitaciones:
                if tipo == habitacion.getTipo():
                    num=habitacion.getNumero()
                    piso=habitacion.getPiso()
                    precio=habitacion.getPrecio()
                    dispo=habitacion.getDisponible()
                    print(f"{num}   {piso}  {precio}    {dispo}")

    def mostrarHabitaciones(self):
        for habitacion in self.__lista_habitaciones:
            print(habitacion)
        