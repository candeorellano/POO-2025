import csv
import numpy as np
from claseInscripcion import Inscripcion

class GestorInscripciones:
    __listaInscripciones:np.ndarray
    __incremento:int
    __dimension:int
    __cantidad:int

    def __init__(self):
        self.__incremento = 3
        self.__dimension = 6
        self.__cantidad = 0
        self.__listaInscripciones = np.empty(self.__dimension, dtype=Inscripcion)

    def agregarInscripcion(self, unaInscripcion):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaInscripciones.resize(self.__dimension)
        self.__listaInscripciones[self.__cantidad] = unaInscripcion
        self.__cantidad += 1

    def cargarArchivo(self):
        archivo = open("inscripciones.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            self.agregarInscripcion(Inscripcion(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4])))
        archivo.close()
    
    def ordenar(self):
        self.__listaInscripciones.sort()

    def buscarInscripto(self, dni):
        i = 0
        encontrado = False

        while i<len(self.__listaInscripciones) and not encontrado:
            if dni.lower() == self.__listaInscripciones[i].getDNI():
                encontrado = True
                nya = self.__listaInscripciones[i].getApellidoYNombre()
                print(f"Nombre y apellido del inscripto: {nya}")
                incremento = 1
                self.__listaInscripciones[i].setDiasAsistencia(incremento)
                print("Se incremento la asistencia!")
            else:
                i += 1

        if not encontrado:
            print("No se encontro el inscripto")


    def inscriptosConAsistenciaMinima(self, idCurso, GC):
        print("Inscriptos con asistencia minima:")
        for inscripcion in self.__listaInscripciones:
            if inscripcion.getIdCurso().lower() == idCurso.lower():
                asistenciaCurso = GC.obtenerDiasAsistencia(inscripcion.getIdCurso())
                minimo = asistenciaCurso * 0.70
                if inscripcion.getDiasAsistencia() >= minimo:
                    dni = inscripcion.getDNI()
                    nombre = inscripcion.getApellidoYNombre()
                    print(f"DNI: {dni} - Nombre: {nombre}")
    
    def mostrarInscripto(self, dni):
        i = 0
        encontrado = False

        while i<len(self.__listaInscripciones) and not encontrado:
            if dni.lower() == self.__listaInscripciones[i].getDNI():
                encontrado = True
                dni = self.__listaInscripciones[i].getDNI()
                nombre = self.__listaInscripciones[i].getApellidoYNombre()
                print(f"DNI: {dni} Nombre y Apellido: {nombre}")
                nota = int(input("Ingrese la nota que obtuvo el inscripto: "))
                self.__listaInscripciones[i].setNotaFinal(nota)
                print("Nota modificada!")
            else:
                i += 1
        
        if not encontrado:
            print("No se encontro el inscripto con ese DNI")

    def inscriptosAprobados(self, idCurso,GC):
        self.ordenar()
        print(f"Inscriptos aprobados en el curso {idCurso}:")
        for inscripcion in self.__listaInscripciones:
            if inscripcion.getIdCurso().lower() == idCurso.lower():
                asistenciaCurso = GC.obtenerDiasAsistencia(inscripcion.getIdCurso())
                minimo = asistenciaCurso * 0.70
                if inscripcion.getNotaFinal() >= 7 and inscripcion.getDiasAsistencia() >= minimo:
                    dni = inscripcion.getDNI()
                    nombre = inscripcion.getApellidoYNombre()
                    print(f"DNI: {dni} - Nombre: {nombre} - Dias de asistencia: {inscripcion.getDiasAsistencia()} - Nota final: {inscripcion.getNotaFinal()}")