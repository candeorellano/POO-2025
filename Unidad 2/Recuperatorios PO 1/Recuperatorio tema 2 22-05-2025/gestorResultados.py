from claseResultado import Resultado
import csv
import numpy as np

class GestorResultados:
    __dimension:int
    __cantidad:int
    __incremento:int
    __listaResultados: np.ndarray

    def __init__(self):
        self.__dimension = 8
        self.__cantidad = 0
        self.__incremento = 8
        self.__listaResultados = np.empty(self.__dimension, dtype=Resultado)
    
    def agregarResultado(self, unResultado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__listaResultados.resize(self.__dimension)
        self.__listaResultados[self.__cantidad] = unResultado
        self.__cantidad += 1

    def cargarArchivo(self):
        archivo = open("resultadosLiguilla.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            self.agregarResultado(Resultado(fila[0], fila[1], int(fila[2]), fila[3], int(fila[4])))
        archivo.close()

    def mostrarEquiposPorFecha(self, fecha, GE):
        i = 0
        encontrado = False
        importeTotal = 0

        print(f"Resultados de la fecha {fecha}:")
        for resultado in self.__listaResultados:
            if resultado.getFecha() == fecha:
                encontrado = True
                idLocal = resultado.getIdEquipoLocal()
                idVisitante = resultado.getIdEquipoVisitante()
                equipoLocal = GE.buscarEquipoPorId(idLocal) #devuelve el nombre del equipo
                equipoVisitante = GE.buscarEquipoPorId(idVisitante)
                importeTotal += (resultado.getValorInscripcion() * 2) #son dos equipos por partido
                print(f"{i+1}. {equipoLocal} {resultado.getGolesLocal()} - {resultado.getGolesVisitante()} {equipoVisitante}")
                i += 1
        print(f"Importe total recaudado por inscripción de los equipos: ${importeTotal}")

        if not encontrado:
            print("No se encontraron resultados para la fecha especificada.")

    def mostrarResultadosPorEquipo(self, idEquipo, GE):
        i = 0
        encontrado = False

        print(f"Resultados de partidos locales del equipo con ID {idEquipo}:")
        for resultado in self.__listaResultados:
            if resultado.getIdEquipoLocal() == idEquipo:
                encontrado = True
                idequipoLocal = resultado.getIdEquipoLocal()
                idequipoVisitante = resultado.getIdEquipoVisitante()
                equipoLocal = GE.buscarEquipoPorId(idequipoLocal)
                equipoVisitante = GE.buscarEquipoPorId(idequipoVisitante)
                print(f"{i+1}. {equipoLocal} Goles: {resultado.getGolesLocal()} - Goles: {resultado.getGolesVisitante()} {equipoVisitante}")
                i += 1

        if not encontrado:
            print("No se encontraron resultados para el equipo especificado.")

    def sumarPuntos(self, GE):

        for resultado in self.__listaResultados:
            if resultado.getGolesLocal() > resultado.getGolesVisitante():
                idLocal = resultado.getIdEquipoLocal()
                GE.acumulaPuntos(idLocal, 3)
            elif resultado.getGolesVisitante() > resultado.getGolesLocal():
                idVisitante = resultado.getIdEquipoVisitante()
                GE.acumulaPuntos(idVisitante, 3)
            else:
                idLocal = resultado.getIdEquipoLocal()
                idVisitante = resultado.getIdEquipoVisitante()
                GE.acumulaPuntos(idLocal, 1)
                GE.acumulaPuntos(idVisitante, 1)
    
    def actualizarGoles(self, GE):
        for resultado in self.__listaResultados:
            idLocal = resultado.getIdEquipoLocal()
            idVisitante = resultado.getIdEquipoVisitante()
            golesLocal = resultado.getGolesLocal()
            golesVisitante = resultado.getGolesVisitante()
            # Local
            GE.actualizaGolesAFavor(idLocal, golesLocal)
            GE.actualizaGolesEnContra(idLocal, golesVisitante)
            # Visitante
            GE.actualizaGolesAFavor(idVisitante, golesVisitante)
            GE.actualizaGolesEnContra(idVisitante, golesLocal)
            # Diferencia
            GE.actualizaDiferenciaGoles(idLocal, golesLocal - golesVisitante)
            GE.actualizaDiferenciaGoles(idVisitante, golesVisitante - golesLocal)