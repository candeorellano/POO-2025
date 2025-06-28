from claseHardware import Hardware
import csv

class ControladorHardware:
    __listaElementosHW:list

    def __init__(self):
        self.__listaElementosHW = []

    def agregarElemento(self, unElemento):
        self.__listaElementosHW.append(unElemento)
    
    def cargarArchivo(self):
        archivo = open("elementosHW.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
            self.agregarElemento(Hardware(fila[0], fila[1], fila[2]))
        archivo.close()

    def buscarElementoPorId(self, id, CT):
        i = 0
        encontrado = False

        while i < len(self.__listaElementosHW) and not encontrado:
            if self.__listaElementosHW[i].getId() == id:
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            elemento = self.__listaElementosHW[i]
            print(f"ID: {elemento.getId()}, Descripcion: {elemento.getDescripcion()}, Ubicacion: {elemento.getUbicacion()}")
            CT.listarTicketsAbiertosPorIdHardware(id)
        else:
            print("Identificador de hardware no encontrado.")

    def buscarUbicacionPorId(self, id):
        i = 0
        encontrado = False
        ubi = ""
        
        while i < len(self.__listaElementosHW) and not encontrado:
            if self.__listaElementosHW[i].getId() == id:
                encontrado = True
                ubi = self.__listaElementosHW[i].getUbicacion()
            else:
                i += 1
        
        return ubi