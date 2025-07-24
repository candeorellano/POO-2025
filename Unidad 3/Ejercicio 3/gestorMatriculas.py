from claseMatricula import Matricula
import csv

class GestorMatriculas:
    __listaMatriculas:list

    def __init__(self):
        self.__listaMatriculas = []

    def agregarMatricula(self, unaMatricula):
        self.__listaMatriculas.append(unaMatricula)
    
    def cargarArchivo(self, ge, gp): #recibe los gestores de empleados y programas
        with open("matriculas.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)

            for fila in reader:
                fecha = fila[0]
                empleado = ge.buscarEmpleado(fila[1]) #busca al empleado en el gestor de empleados
                programa = gp.buscarPrograma(fila[2]) #busca al programa en el gestor de programas
                if (empleado is not None and programa is not None):
                    matricula = Matricula(fecha, empleado, programa)
                    self.agregarMatricula(matricula)
            archivo.close()

    def inciso1(self, id):
        encontrado = False
        for matricula in self.__listaMatriculas:
            if id == matricula.getEmpleado().getId():
                if encontrado == False:
                    print(f"Nombre del empleado: {matricula.getEmpleado().getNyA()}")
                    encontrado = True
                # Si ya se encontró al empleado, no repetir el nombre
                prog = matricula.getPrograma().getNombre()
                dur = matricula.getPrograma().getDuracion()
                print(f"Programa: {prog} - Duracion: {dur}")
        
        if not encontrado:
            raise IndexError
    
    def inciso2(self, nom):
        encontrado = False
        print(f"Empleados matriculados en el programa de capacitacion '{nom}': ")
        for matricula in self.__listaMatriculas:
            if nom.strip().lower() == matricula.getPrograma().getNombre().strip().lower():
                encontrado = True
                empleado = matricula.getEmpleado()
                print(f"{empleado}")
        
        if not encontrado:
            print("No se encontro el programa de capacitacion ingresado.")
        
    def listarMatriculas(self):
        for matricula in self.__listaMatriculas:
            print(matricula)

    def buscarEmpleado(self, empleado):
        i = 0
        encontrado = False

        while i < len(self.__listaMatriculas) and not encontrado:
            if empleado == self.__listaMatriculas[i].getEmpleado().getNyA():
                encontrado = True
            else:
                i += 1

        return encontrado