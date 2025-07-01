import csv
from claseCurso import Curso

class GestorCursos:
    __listaCursos:list

    def __init__(self):
        self.__listaCursos = []

    def agregar(self, unCurso):
        self.__listaCursos.append(unCurso)
    
    def cargarArchivo(self):
        archivo = open("cursos.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            self.agregar(Curso(fila[0], fila[1], int(fila[2]), int(fila[3]), int(fila[4])))
        archivo.close()

    def mostrarInscriptosConAsistenciaMinima(self, idCurso, GI, GC):
        i = 0
        encontrado = False

        while i < len(self.__listaCursos) and not encontrado:
            if idCurso.lower() == self.__listaCursos[i].getId():
                encontrado = True
                print(f"Curso encontrado: {self.__listaCursos[i].getDenominacion()}")
                GI.inscriptosConAsistenciaMinima(idCurso, GC)
            else:
                i += 1
        if not encontrado:
            print("Curso no encontrado")
    
    def obtenerDiasAsistencia(self, idCurso):
        i = 0
        encontrado = False

        while i < len(self.__listaCursos) and not encontrado:
            if idCurso.lower() == self.__listaCursos[i].getId().lower():
                encontrado = True
                dias = self.__listaCursos[i].getDias()
            else:
                i += 1
        
        return dias

    def listarCursos(self, GI, GC):
        for curso in self.__listaCursos:
            deno = curso.getDenominacion()
            cupo = curso.getCupo()
            print(f"Denominacion: {deno} - Cupo Maximo: {cupo}")
            idCurso = curso.getId()
            GI.inscriptosAprobados(idCurso, GC)