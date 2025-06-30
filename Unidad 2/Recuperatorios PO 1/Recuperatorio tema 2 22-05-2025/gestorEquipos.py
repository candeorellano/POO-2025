from claseEquipo import Equipo
import csv

class GestorEquipos:
    __listaEquipos: list

    def __init__(self):
        self.__listaEquipos = []

    def agregarEquipo(self, unEquipo):
        self.__listaEquipos.append(unEquipo)

    def cargarArchivo(self):
        archivo = open("equiposLiguilla.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)  
        for fila in reader:
            self.agregarEquipo(Equipo(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5])))
        archivo.close()

    def buscarEquipoPorId(self, id):
        i = 0
        encontrado = False
        while i < len(self.__listaEquipos) and not encontrado:
            if self.__listaEquipos[i].getId() == id:
                encontrado = True
            else:
                i += 1
        
        if encontrado:
            return self.__listaEquipos[i].getDenominacion()
        
    def mostrarResultadosEquipo(self, equipo, GR, GE):
        i = 0
        encontrado = False
        
        while i < len(self.__listaEquipos) and not encontrado:
            if self.__listaEquipos[i].getDenominacion().lower() == equipo.lower():
                encontrado = True
                idEquipo = self.__listaEquipos[i].getId()
                GR.mostrarResultadosPorEquipo(idEquipo, GE)
            else:
                i += 1

        if not encontrado:
            print("No se encontro el equipo especificado.")
        
    def ordenar(self):
        self.__listaEquipos = sorted(self.__listaEquipos, reverse=True)

    def acumulaPuntos(self, id, puntos):
        i = 0
        encontrado = False

        while i < len(self.__listaEquipos) and not encontrado:
            if id == self.__listaEquipos[i].getId():
                encontrado = True
                self.__listaEquipos[i].setPuntos(puntos)
            else:
                i += 1
    
    def actualizaGolesAFavor(self, id, goles):
        i = 0
        encontrado = False

        while i < len(self.__listaEquipos) and not encontrado:
            if id == self.__listaEquipos[i].getId():
                encontrado = True
                self.__listaEquipos[i].setGolesAFavor(goles)
            else:
                i += 1
    
    def actualizaGolesEnContra(self, id, goles):
        i = 0
        encontrado = False

        while i < len(self.__listaEquipos) and not encontrado:
            if id == self.__listaEquipos[i].getId():
                encontrado = True
                self.__listaEquipos[i].setGolesEnContra(goles)
            else:
                i += 1
    
    def actualizaDiferenciaGoles(self, id, diferencia):
        i = 0
        encontrado = False

        while i < len(self.__listaEquipos) and not encontrado:
            if id == self.__listaEquipos[i].getId():
                encontrado = True
                self.__listaEquipos[i].setDiferenciaGoles(diferencia)
            else:
                i += 1
    
    def mostrarTabla(self):
        self.ordenar()
        i = 1
        print("Tabla de posiciones:")
        print(f"Posicion    Equipo  Puntos  Goles a Favor  Goles en Contra  Diferencia de Goles")
        for equipo in self.__listaEquipos:
            nomEquipo = equipo.getDenominacion()
            puntos = equipo.getPuntos()
            golesAFavor = equipo.getGolesAFavor()
            golesEnContra = equipo.getGolesEnContra()
            diferenciaGoles = equipo.getDiferenciaGoles()
            print(f"{i}   {nomEquipo}  {puntos}  {golesAFavor}  {golesEnContra}  {diferenciaGoles}")
            i += 1