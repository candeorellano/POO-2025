from claseMedio import Medio
from clasePrensa import Prensa
from claseRadio import Radio
from clasePrograma import Programa
import csv

class GestorMedios:
    __listaMedios:list

    def __init__(self):
        self.__listaMedios = []

    def agregaMedio(self, unMedio):
        if isinstance(unMedio, Medio):
            self.__listaMedios.append(unMedio)
        else:
            raise TypeError("El objeto no es una instancia de la clase Medio o sus subclases.")
        
    def leeArchivo(self):
        archivoMedios = open("Medios.csv")
        readerMedios = csv.reader(archivoMedios, delimiter=',')
        archivoProgramas = open("Programas.csv")
        readerProgramas = csv.reader(archivoProgramas, delimiter=',')

        for filaM in readerMedios:
            if filaM[0] == "R":
                unMedio = Radio(filaM[1], int(filaM[2]), filaM[3])
                for filaP in readerProgramas:
                    if filaP[0] == filaM[3]:
                        unMedio.agregaPrograma(filaP[1], filaP[2], filaP[3]) #Composicion
                self.agregaMedio(unMedio)
                archivoProgramas.seek(0)  # Reiniciar el cursor del archivo de programas
            elif filaM[0] == "P":
                unMedio = Prensa(filaM[1], int(filaM[2]), filaM[3], int(filaM[4]))
                self.agregaMedio(unMedio)
        archivoMedios.close()
        archivoProgramas.close()
        print("Medios y programas cargados correctamente.")
    
    def mostrarDatosPrograma(self, nombrePrograma):
        i = 0
        encontrado = False

        while i < len(self.__listaMedios) and not encontrado:
            medio = self.__listaMedios[i]
            if isinstance(medio, Radio):
                prog = medio.buscarPrograma(nombrePrograma)
                if prog:
                    print(f"Medio de comunicación: {medio.getNombre()}")
                    print(f"Frecuencia: {medio.getFrecuencia()}")
                    print(f"Programa: {prog.getNombre()}")
                    print(f"Horario de transmisión: {prog.getHoraInicio()} - {prog.getHoraFin()}")
                    encontrado = True
                else:
                    i += 1 #si el programa no esta en ese medio, se pasa al siguiente
            else:
                i += 1
        
        if not encontrado:
            raise Exception
        
    def mostrarMedios(self):
        for medio in self.__listaMedios:
            print(medio)