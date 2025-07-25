from claseNodo import NodoMedio
import csv
from claseTelevision import Television
from clasePrograma import Programa
from claseRadio import Radio
from clasePrensa import Prensa

class GestorMedios:
    __comienzo: NodoMedio
    __actual: NodoMedio
    __indice:int
    __tope:int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            medio = self.__actual.getMedio()
            self.__actual = self.__actual.getSiguiente()
            return medio
    
    def agregarMedio(self, unMedio):
        nodo = NodoMedio(unMedio)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def leeArchivos(self):
        archivoMedios = open("medios.csv", encoding='utf-8')
        readerMedios  = csv.reader(archivoMedios, delimiter=';')
        archivoProgramas = open("programa.csv", encoding='utf-8')
        readerProgramas = csv.reader(archivoProgramas, delimiter=';')
        next(readerMedios)  # Skip header
        next(readerProgramas)  # Skip header

        for filaMedios in readerMedios:
            if filaMedios[0] == "T":
                television = Television(filaMedios[1], int(filaMedios[2]), int(filaMedios[3]), filaMedios[4])

                for filaProgramas in readerProgramas:
                    if str(filaProgramas[1]) == str(filaMedios[3]):
                        television.agregaPrograma(Programa(filaProgramas[2], filaProgramas[3], filaProgramas[4]))
                archivoProgramas.seek(0)  # Reset file pointer for next medium
                readerProgramas = csv.reader(archivoProgramas, delimiter=';')
                next(readerProgramas)
                self.agregarMedio(television)
            elif filaMedios[0] == "R":
                radio = Radio(filaMedios[1], int(filaMedios[2]), filaMedios[5], filaMedios[6])

                for filaProgramas in readerProgramas:
                    if str(filaProgramas[1]) == str(filaMedios[6]):
                        radio.agregaPrograma(Programa(filaProgramas[2], filaProgramas[3], filaProgramas[4]))
                archivoProgramas.seek(0)
                readerProgramas = csv.reader(archivoProgramas, delimiter=';')
                next(readerProgramas)
                self.agregarMedio(radio)
            elif filaMedios[0] == "P":
                self.agregarMedio(Prensa(filaMedios[1], int(filaMedios[2]), filaMedios[7], filaMedios[8]))
            
        archivoMedios.close()
        archivoProgramas.close()
        print("Medios y programas cargados correctamente.")

    def inciso1(self, pos):
        if pos < 0 or pos > self.__tope:
            raise IndexError
        else:
            unMedio = self.leeMedioManual()
            if pos == 0:
                self.agregarMedio(unMedio)
            else:
                aux = self.__comienzo
                for i in range(pos - 1):
                    aux = aux.getSiguiente()
                nodo = NodoMedio(unMedio)
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
                self.__tope += 1
    
    def leeMedioManual(self):
        medio = None
        tipo = input("Ingrese el tipo de medio (T: Television, R: Radio, P: Prensa): ").lower()
        if tipo in ['t', 'r', 'p']:
            nombre = input("Ingrese el nombre del medio: ")
            audiencia = int(input("Ingrese la audiencia del medio: "))
            if tipo == 't':
                canales = int(input("Ingrese la cantidad de canales: "))
                canal = input("Ingrese número de canal: ")
                medio = Television(nombre, audiencia, canales, canal)
                bandera = input("¿Desea agregar programas a la televisión? (si/no): ").lower()
                while bandera != "no":
                    nombrePrograma = input("Ingrese el nombre del programa: ")
                    horaInicio = input("Ingrese el horario de inicio del programa: ")
                    horaFin = input("Ingrese la hora de finalización del programa: ")
                    medio.agregaPrograma(Programa(nombrePrograma, horaInicio, horaFin))
                    bandera = input("¿Desea agregar otro programa? (si/no): ").lower()
            elif tipo == 'r':
                emisora = input("Ingrese nombre de la emisora: ")
                frecuencia = input("Ingrese la frecuencia: ")
                medio = Radio(nombre, audiencia, emisora, frecuencia)
                bandera = input("¿Desea agregar programas a la radio? (si/no): ").lower()
                while bandera != "no":
                    nombrePrograma = input("Ingrese el nombre del programa: ")
                    horaInicio = input("Ingrese el horario de inicio del programa: ")
                    horaFin = input("Ingrese la hora de finalización del programa: ")
                    medio.agregaPrograma(Programa(nombrePrograma, horaInicio, horaFin))
                    bandera = input("¿Desea agregar otro programa? (si/no): ").lower()
            elif tipo == 'p':
                tipoPublicacion = input("Ingrese el tipo de publicación (Diario/Revista): ")
                periodicidad = input("Ingrese la periodicidad: ")
                medio = Prensa(nombre, audiencia, tipoPublicacion, periodicidad)
        else:
            raise TypeError("Tipo de medio no válido. Debe ser 'T', 'R' o 'P'.")
        return medio #devuelve el medio creado
    
    def inciso2(self):
        unMedio = self.leeMedioManual()
        if isinstance(unMedio, Television) or isinstance(unMedio, Radio) or isinstance(unMedio, Prensa):
            self.agregarMedio(unMedio)
            print("Medio agregado correctamente.")
        else:
            raise TypeError

    def mostrarCanalYHorario(self, prog):
        encontrado = False
        aux = self.__comienzo
        programa = None

        while aux != None and not encontrado:
            if isinstance(aux.getMedio(), Television):
                programa = aux.getMedio().buscarPrograma(prog)
            if programa:
                print(f"{aux.getMedio()}")
                print(f"{programa}")
                encontrado = True
            else:
                aux = aux.getSiguiente()
        
        if not encontrado:
            print(f"El programa '{prog}' no se encontró en ninguna televisión.")
    
    def listarProgramacionEmisora(self, emi):
        encontrado = False
        aux = self.__comienzo
        emisora = None

        while aux != None and not encontrado:
            if isinstance(aux.getMedio(), Radio) and aux.getMedio().getEmisora().lower() == emi.lower():
                emisora = aux.getMedio()
                encontrado = True
                aux = None
                emisora.muestraProgramacion()
            else:
                aux = aux.getSiguiente()
        
        if not encontrado:
            print(f"La emisora de radio '{emi}' no se encontró en la colección.")
    
    def contarDiariosYRevistas(self):
        contDiarios = 0
        contRevistas = 0
        aux = self.__comienzo

        while aux != None:
            if isinstance(aux.getMedio(), Prensa):
                if aux.getMedio().getTipoPublicacion().lower() == "diario":
                    contDiarios += 1
                elif aux.getMedio().getTipoPublicacion().lower() == "revista":
                    contRevistas += 1
            aux = aux.getSiguiente()

        print(f"Cantidad de diarios: {contDiarios}")
        print(f"Cantidad de revistas: {contRevistas}")

    def listarMedios(self):
        aux = self.__comienzo
        if aux is None:
            print("No hay medios en la colección.")
        while aux != None:
            medio = aux.getMedio()
            print(medio)
            if isinstance(medio,Television) or isinstance(medio, Radio):
                medio.muestraProgramacion()
            aux = aux.getSiguiente()
