from gestorMatriculas import GestorMatriculas
from gestorProgramas import GestorProgramas
from gestorEmpleados import GestorEmpleados

def menu():
    opcion=int(input("""MENU DE OPCIONES
                [1] Informar la duración de todos los programas de capacitación en los que está matriculado un empleado.
                [2] Mostrar los empleados matriculados en un programa de capacitacion.
                [3] Mostrar empleados que no han sido matriculados en ningun programa de capacitacion.
                [4] Listar matriculas (para verificar) 
                --> """))
    return opcion

if __name__=='__main__':
    GP = GestorProgramas()
    GP.cargarArchivo()
    GE = GestorEmpleados()
    GE.cargarArchivo()
    GM =  GestorMatriculas()
    GM.cargarArchivo(GE, GP)
    op = menu()

    while op != 0:
        if op == 1:
            try:
                id = int(input("Indique el ID del empleado: "))
                GM.inciso1(id)
            except ValueError:
                print("Error. Se esperaba un numero entero")
            except IndexError:
                print("Error. ID no encontrado")
        elif op == 2:
            nombre = input("Indique el nombre del programa de capacitacion: ")
            GM.inciso2(nombre)
        elif op == 3:
            GE.inciso3(GM)
        elif op == 4:
            GM.listarMatriculas()
        else:
            print("Opcion incorrecta. Intente de nuevo")
        op = menu()
    print("Saliendo...")
    