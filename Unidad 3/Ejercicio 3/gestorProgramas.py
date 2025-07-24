from clasePrograma import Programa
import csv

class GestorProgramas:
    __listaProgramas:list

    def __init__(self):
        self.__listaProgramas = []

    def agregarPrograma(self, unPrograma):
        self.__listaProgramas.append(unPrograma)
    
    def cargarArchivo(self):
        with open("programas.csv", encoding="utf-8") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)

            for fila in reader:
                self.agregarPrograma(Programa(fila[0], fila[1], int(fila[2])))
            archivo.close()
    
    def buscarPrograma(self, programa):
        i = 0
        encontrado = False
        obj=None
        
        while i<len(self.__listaProgramas) and not encontrado:
            if programa == self.__listaProgramas[i].getNombre():
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            obj=self.__listaProgramas[i]
        
        return obj