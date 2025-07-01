from gestorCursos import GestorCursos
from gestorInscripciones import GestorInscripciones

#Candela Victoria Orellano Tobares 45545903 Registro:E010-320
def menu():
    op = int(input("""MENU DE OPCIONES
                   [1] Mostrar nombre y apellido de un inscripto e incrementar la cantidad de dias que asistio
                   [2] Mostrar datos de los inscriptos que alcanzaron el procentaje minimo de asistencias
                   [3] Mostrar datos de un inscripto y modificar nota final
                   [4] Listar inscriptos que aprobaron cada curso
                   [0] SALIR
                   Indique su opcion ->"""))
    
    return op

if __name__ == "__main__":
    GC = GestorCursos()
    GC.cargarArchivo()
    GI = GestorInscripciones()
    GI.cargarArchivo()

    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            dni = input("Ingrese el dni del inscripto: ")
            GI.buscarInscripto(dni)
        elif opcion == 2:
            idCurso = input("Ingrese el ID del curso: ")
            GC.mostrarInscriptosConAsistenciaMinima(idCurso, GI, GC)
        elif opcion == 3:
            dni = input("Ingrese el dni del inscripto: ")
            GI.mostrarInscripto(dni)
        elif opcion == 4:
            GC.listarCursos(GI,GC)
        else:
            print("Opcion no valida, intente nuevamente.")
        opcion = menu()
    print("Saliendo del programa...")