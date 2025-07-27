from clasePaciente import Paciente

class PacienteHospitalizado(Paciente):
    __habitacion:int
    __fechaIngreso:str
    __diagnostico:str
    __diasHospitalizado:int
    __importeDescartables:int

    def __init__(self, nom, apell, email, tel, habitacion, fechaIngreso, diagnostico, diasHospitalizado, importeDescartables):
        super().__init__(nom, apell, email, tel)
        self.__habitacion = habitacion
        self.__fechaIngreso = fechaIngreso
        self.__diagnostico = diagnostico
        self.__diasHospitalizado = diasHospitalizado
        self.__importeDescartables = importeDescartables

    def getHabitacion(self):
        return self.__habitacion
    
    def getFechaIngreso(self):
        return self.__fechaIngreso
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def getDiasHospitalizado(self):
        return self.__diasHospitalizado
    
    def getImporteDescartables(self):
        return self.__importeDescartables
    
    def getImporte(self):
        importe = self.getConsulta() * self.getDiasHospitalizado() + self.getImporteDescartables()
        return importe

    def __str__(self):
        return (super().__str__() + 
                f", Habitacion: {self.getHabitacion()}, Fecha Ingreso: {self.getFechaIngreso()}, Diagnostico: {self.getDiagnostico()}, "
                f"Dias Hospitalizado: {self.getDiasHospitalizado()}, Importe Descartables: {self.getImporteDescartables()}")
    