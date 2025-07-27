from clasePaciente import Paciente

class PacienteAmbulatorio(Paciente):
    __historial: str
    __alergias: str
    __obraSocial: str

    def __init__(self, nom, apell, email, tel, historial, alergias, obraSocial):
        super().__init__(nom, apell, email, tel)
        self.__historial = historial
        self.__alergias = alergias
        self.__obraSocial = obraSocial

    def getHistorial(self):
        return self.__historial
    
    def getAlergias(self):
        return self.__alergias
    
    def getObraSocial(self):
        return self.__obraSocial
    
    def getImporte(self):
        if self.getObraSocial() == "Provincia":
            importe = self.getConsulta() - 15000 + 5000 #se resta el valor de la consulta y se suma un plus de 5000
        elif self.getObraSocial() == "OSDE":
            importe = self.getConsulta() - 15000 + 2000 #se resta el valor de la consulta y se suma un plus de 2000
        else:
            importe = self.getConsulta() - 15000 + 10000 #se resta el valor de la consulta y se suma un plus de 10000
        return importe

    def __str__(self):
        return (super().__str__() + 
                f", Historial: {self.getHistorial()}, Alergias: {self.getAlergias()}, Obra Social: {self.getObraSocial()}")