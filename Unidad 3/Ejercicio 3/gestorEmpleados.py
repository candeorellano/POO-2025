from claseEmpleado import Empleado
import csv

class GestorEmpleados:
    __listaEmpleados:list

    def __init__(self):
        self.__listaEmpleados = []

    def agregarEmpleado(self, unEmpleado):
        self.__listaEmpleados.append(unEmpleado)
    
    def cargarArchivo(self):
        with open("empleados.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)

            for fila in reader:
                self.agregarEmpleado(Empleado(fila[0], int(fila[1]), fila[2]))
            archivo.close()

    def buscarEmpleado(self, empleado):
        i = 0
        encontrado = False
        obj=None

        while i<len(self.__listaEmpleados) and not encontrado:
            if empleado == self.__listaEmpleados[i].getNyA():
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            obj=self.__listaEmpleados[i]
        
        return obj
    
    def inciso3(self, gm):
        encontrado = False
        print("Empleados que no han sido matriculados en ningun programa de capacitacion:")
        for empleado in self.__listaEmpleados:
            matriculado = gm.buscarEmpleado(empleado.getNyA())
            if not matriculado:
                encontrado = True
                print(empleado)
        
        if not encontrado:
            print("Todos los empleados han sido matriculados en al menos un programa de capacitacion.")