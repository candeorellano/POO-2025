from claseTicket import Ticket
import csv
import numpy as np

class ControladorTickets:
    __cantidad:int
    __dimension:int
    __incremento:int
    __listaTickets:np.ndarray

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 4
        self.__incremento = 4
        self.__listaTickets = np.empty(self.__dimension, dtype=Ticket)

    def agregarTicket(self, unTicket):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaTickets.resize(self.__dimension)
        self.__listaTickets[self.__cantidad] = unTicket
        self.__cantidad += 1
    
    def cargarArchivo(self):
        archivo = open("tickets.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
            self.agregarTicket(Ticket(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))
        archivo.close()

    def listarTicketsAbiertosPorIdHardware(self, id):
        print(f"Tickets abiertos para el ID de hardware {id}:")
        for ticket in self.__listaTickets:
            if ticket.getIdHardware() == id and ticket.getFechaEntrega() == "": # "" porque tiene que estar sin fecha de entrega
                print(ticket)

    def listarTicketsPorId(self, id, CHW):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__listaTickets[i].getIdTicket() == id:
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            ticket = self.__listaTickets[i]
            id_hw = ticket.getIdHardware()
            descripcion = ticket.getDescripcion()
            ubicacion = CHW.buscarUbicacionPorId(id_hw)
            fechaPedido = ticket.getFechaPedido()
            print(f"ID Hardware: {id_hw}, Descripcion: {descripcion}, Ubicacion: {ubicacion}, Fecha de Pedido: {fechaPedido}")
        else:
            print("Identificador de ticket no encontrado.")

    def buscarTicketAbiertoPorId(self, id):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__listaTickets[i].getIdTicket() == id and self.__listaTickets[i].getFechaEntrega() == "":
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            ticket = self.__listaTickets[i]
            fechaEntrega = input("Ingrese la fecha de finalizacion del ticket: (DD/MM/AAAA): ")
            tecnico = input("Ingrese el nombre del tecnico: ")
            ticket.setFechaEntrega(fechaEntrega)
            ticket.setTecnico(tecnico)
            print(f"Ticket actualizado: {ticket}") #muestra el ticket actualizado
        else:
            print("Identificador de ticket abierto no encontrado.")
        
    def listarTicketsPorTipoServicio(self, tipoServicio):
        print(f"Tickets de tipo {tipoServicio}:")
        for i in range(self.__cantidad):
            ticket = self.__listaTickets[i]
            if ticket.getServicio().lower() == tipoServicio.lower(): # compara el tipo de servicio del ticket (definido por __eq__)
                print(ticket)