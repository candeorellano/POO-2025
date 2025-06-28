class Ticket:
    __idTicket:str
    __idHardware:str
    __descripcion:str
    __servicio:str
    __fechaPedido:str
    __fechaEntrega:str
    __tecnico:str

    def __init__(self, idTicket, idHardware, desc, servicio, fechaPedido, fechaEntrega="", tecnico=""):
        self.__idTicket = idTicket
        self.__idHardware = idHardware
        self.__descripcion = desc
        self.__servicio = servicio
        self.__fechaPedido = fechaPedido
        self.__fechaEntrega = fechaEntrega #puede ser una cadena vacía si no se ha entregado
        self.__tecnico = tecnico #puede ser una cadena vacía si no se ha asignado un técnico

    def getIdTicket(self):
        return self.__idTicket
    
    def getIdHardware(self):
        return self.__idHardware
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getServicio(self):
        return self.__servicio
    
    def getFechaPedido(self):
        return self.__fechaPedido
    
    def getFechaEntrega(self):
        return self.__fechaEntrega
    
    def getTecnico(self):
        return self.__tecnico
    
    def setFechaEntrega(self, fecha):
        self.__fechaEntrega = fecha
    
    def setTecnico(self, tecnico):
        self.__tecnico = tecnico

    def __str__(self):
        return (f"ID Ticket: {self.__idTicket}, ID Hardware: {self.__idHardware}, "
                f"Descripcion: {self.__descripcion}, Servicio: {self.__servicio}, "
                f"Fecha Pedido: {self.__fechaPedido}, Fecha Entrega: {self.__fechaEntrega}, "
                f"Tecnico: {self.__tecnico}")
    
    def __eq__(self, servicio):
        return self.__servicio == servicio