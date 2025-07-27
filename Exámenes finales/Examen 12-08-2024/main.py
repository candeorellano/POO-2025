from gestorPacientes import GestorPacientes

def menu():
    op = int(input("""MENU DE OPCIONES:
                   [1] Insertar objetos al final de la colección
                   [2] Indicar la cantidad de pacientes hospitalizados, cuyo diagnostico sea "Neumonía", y la 
                   cantidad de pacientes ambulatorios
                   [3] Mostrar el importe cobrado por la clinica a todos los pacientes
                   [4] Indicar que tipo de paciente se encuentra en una posicion dada de la colección
                   [5] Modificar el valor de consulta
                   [0] SALIR
                   Ingrese una opción: """))
    return op

if __name__ == '__main__':
    gp = GestorPacientes()
    
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            gp.leeArchivo() #cargar pacientes desde el archivo
            for paciente in gp:
                print(paciente)
        elif opcion == 2:
            gp.cantHospitalizadosNeumonia()
            gp.cantAmbulatorios()
        elif opcion == 3:
            gp.mostrarImporteCobrado()
        elif opcion == 4:
            try:
                pos = int(input("Ingrese la posición del paciente: "))
                gp.mostrarPacientePorPosicion(pos)
            except IndexError:
                print("Índice fuera de rango.")
        elif opcion == 5:
            try:
                valor = int(input("Ingrese el nuevo valor de consulta: "))
                gp.modificarValorConsulta(valor)
            except ValueError:
                print("Valor no válido. Debe ser un número entero.")
        else:
            print("Opción no válida. Intente nuevamente.")
        opcion = menu()
    print("Saliendo del programa...")