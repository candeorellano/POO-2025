from clasePaciente import Paciente
from pacienteHospitalizado import PacienteHospitalizado
from pacienteAmbulatorio import PacienteAmbulatorio
from claseNodo import NodoPaciente
import csv

class GestorPacientes:
    __comienzo: NodoPaciente
    __actual: NodoPaciente
    __tope: int
    __indice: int

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            paciente = self.__actual.getPaciente()
            self.__actual = self.__actual.getSiguiente()
            return paciente

    def agregarPaciente(self, unPaciente):
        nodo = NodoPaciente(unPaciente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    #inciso 1
    def leeArchivo(self):
        archivo = open("pacientes.csv", encoding="utf-8")
        reader = csv.reader(archivo, delimiter=',')

        for fila in reader:
            if fila[0] == 'P':
                paciente = Paciente(fila[1], fila[2], fila[3], fila[4])
                self.agregarPaciente(paciente)
            elif fila[0] == 'O':
                paciente = PacienteAmbulatorio(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
                self.agregarPaciente(paciente)
            elif fila[0] == 'H':
                paciente = PacienteHospitalizado(fila[1], fila[2], fila[3], fila[4], int(fila[5]), fila[6], fila[7], int(fila[8]), int(fila[9]))
                self.agregarPaciente(paciente)
        archivo.close()
        print("Pacientes cargados desde el archivo 'pacientes.csv'.")

    #inciso 2
    def cantHospitalizadosNeumonia(self):
        cont = 0
        aux = self.__comienzo

        while aux is not None:
            if isinstance(aux.getPaciente(), PacienteHospitalizado):
                if aux.getPaciente().getDiagnostico() == "Neumonía":
                    cont += 1
            aux = aux.getSiguiente()
        print(f"Cantidad de pacientes hospitalizados con diagnóstico de Neumonía: {cont}")
    
    def cantAmbulatorios(self):
        cont = 0
        aux = self.__comienzo

        while aux is not None:
            if isinstance(aux.getPaciente(), PacienteAmbulatorio):
                cont += 1
            aux = aux.getSiguiente()
        print(f"Cantidad de pacientes ambulatorios: {cont}")

    def mostrarImporteCobrado(self):
        aux = self.__comienzo
        print("Importe cobrado por la clínica a todos los pacientes:")
        while aux is not None:
            paciente = aux.getPaciente()
            importe = paciente.getImporte()
            print(f"{paciente.getNombre()} {paciente.getApellido()}: ${importe}")
            aux = aux.getSiguiente()

    def mostrarPacientePorPosicion(self, pos):
        if pos < 0 or pos >= self.__tope: #las posiciones van del 0 al 6 segun el archivo
            raise IndexError
        else:
            aux = self.__comienzo
            for i in range(pos):
                aux = aux.getSiguiente()
            if isinstance(aux.getPaciente(), PacienteHospitalizado):
                print(f"Paciente en posición {pos} es de tipo Hospitalizado")
            elif isinstance(aux.getPaciente(), PacienteAmbulatorio):
                print(f"Paciente en posición {pos} es de tipo Ambulatorio")
            else:
                print(f"Paciente en posición {pos} es de tipo General")
    
    def modificarValorConsulta(self, nuevoImporte):
        Paciente.setConsulta(nuevoImporte)
        print(f"Valor de consulta modificado a: ${nuevoImporte}")
        self.mostrarImporteCobrado()  # Mostrar los importes actualizados después de modificar el valor de consulta