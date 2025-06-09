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
    
    def agregarHabitacion(self, num, piso, tipo, precio, dispo):
        unaHabitacion = Habitacion(num,piso,tipo,precio,dispo)
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

    #OTROS METODOS

    def buscaHabPorNum(self, xnum):
        i = 0
        encontrado = False

        while i<len(self.__lista_habitaciones) and not encontrado:
            if xnum == self.__lista_habitaciones[i].getNumero():
                encontrado = True
            else:
                i+=1
        
        if encontrado:
            return i
        else:
            raise ValueError("Habitacion no encontrada")
        
    def getDisponibilidad(self, i):
        disponibilidad = self.__lista_habitaciones[i].getDisponibilidad()
        return disponibilidad
    
    def reservarHabitacion(self, i):
        self.__lista_habitaciones[i].setDisponibilidad()
        
    def liberarHabitacion(self, i):
        self.__lista_habitaciones[i].setDisponibilidad()
    
    def muestraHabPorTipo(self, xtipo):
        for habitacion in self.__lista_habitaciones:
            if xtipo == habitacion.getTipo():
                print(f"Numero Habitacion: {habitacion.getNumero()} - Piso: {habitacion.getPiso()}")
    
    def contarHabLibres(self):
        cont = 0
        for habitacion in self.__lista_habitaciones:
            if habitacion.getDisponibilidad == True:
                cont +=1
        
        return cont
    
    def listaTipos(self):
        tipos = []
        for habitacion in self.__lista_habitaciones:
            xtipo = habitacion.getTipo()
            if xtipo not in tipos:
                tipos.append(xtipo)
        return tipos
    
    def mostrarDetalles(self):
        tiposHab = self.listaTipos()

        for tipo in tiposHab:
            print(f"Tipo de habitacion: {tipo}")
            print("Numero   Piso    Precio por Noche    Disponibilidad")
            for habitacion in self.__lista_habitaciones:
                if tipo == habitacion.getTipo():
                    num=habitacion.getNumero()
                    piso=habitacion.getPiso()
                    precio=habitacion.getPrecio()
                    dispo=habitacion.getDisponibilidad()
                    print(f"{num}   {piso}  {precio}    {dispo}")
    
    def mostrarHabitaciones(self):
        for habitacion in self.__lista_habitaciones:
            print(habitacion)