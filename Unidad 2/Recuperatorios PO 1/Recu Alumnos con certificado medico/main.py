from controladorHardware import ControladorHardware
from controladorTickets import ControladorTickets

def menu():
    op = int(input("""Menu de opciones: 
                   [1]Listar descripcion, ubicacion y tickets abiertos de un elemento de hardware
                   [2]Listar identificador de hardware, descripcion, ubicacion y fecha de pedido de un ticket
                   [3]Solicitar fecha de finalizacion y nombre del tecnico de un ticket abierto
                   [4]Mostrar tickets por tipo de servicio
                   [0]Salir
                   Ingrese una opcion: """))
    return op

if __name__=='__main__':
    controladorHW = ControladorHardware()
    controladorHW.cargarArchivo()
    
    controladorTickets = ControladorTickets()
    controladorTickets.cargarArchivo()
    
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            id_hw = input("Ingrese el ID del elemento de hardware: ")
            controladorHW.buscarElementoPorId(id_hw, controladorTickets)
        elif opcion == 2:
            id_ticket = input("Ingrese el ID del ticket: ")
            controladorTickets.listarTicketsPorId(id_ticket, controladorHW)
        elif opcion == 3:
            id_ticket = input("Ingrese el ID del ticket abierto: ")
            controladorTickets.buscarTicketAbiertoPorId(id_ticket)
        elif opcion == 4:
            tipo_servicio = input("Ingrese el tipo de servicio (hardware, software, red): ")
            controladorTickets.listarTicketsPorTipoServicio(tipo_servicio)
        else:
            print("Opcion no valida. Intente nuevamente.")
        opcion = menu()
    print("Saliendo del programa...")
            