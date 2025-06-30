# Orellano Tobares, Candela Victoria
#Registro: E010-320

from gestorEquipos import GestorEquipos
from gestorResultados import GestorResultados

def menu():
    op = int(input("""               Menu de Opciones:
                   [1] Mostrar los equipos con sus resultados obtenidos en una fecha determinada 
                   y mostrar el importe recaudado por la inscripcion de los equipos.
                   [2] Mostrar resultados de los partidos locales que jugo un equipo.
                   [3] Mostrar tabla de posiciones.
                   [0] SALIR
                   -> """))
    return op

if __name__ == '__main__':
    GE = GestorEquipos()
    GR = GestorResultados()
    GE.cargarArchivo()
    GR.cargarArchivo()
    opcion = menu()

    while(opcion != 0):
        if opcion == 1:
            fecha = input("Ingrese la fecha: ")
            GR.mostrarEquiposPorFecha(fecha, GE)
        elif opcion == 2:
            equipo = input("Ingrese el nombre del equipo: ")
            GE.mostrarResultadosEquipo(equipo, GR, GE)
        elif opcion == 3:
            GR.sumarPuntos(GE)
            GR.actualizarGoles(GE)
            GE.mostrarTabla()
        else:
            print("Opcion incorrecta. Intente de nuevo")
        opcion = menu()
    print("Saliendo del programa...")