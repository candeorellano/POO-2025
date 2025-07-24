from clasePlan import Plan

class PlanTelevision(Plan):
    __nacionales:int
    __internacionales:int

    def __init__(self, comp, dur, cob, pb, nacionales, internacionales):
        super().__init__(comp, dur, cob, pb)
        self.__nacionales = nacionales
        self.__internacionales = internacionales

    def getNacionales(self):
        return self.__nacionales
    
    def getInternacionales(self):
        return self.__internacionales
    
    def __str__(self):
        return f"{super().__str__()}, Canales nacionales: {self.__nacionales}, Canales internacionales: {self.__internacionales}"
    
    def getImporteFinal(self):
        base = self.getPrecioBase()
        importe = self.getPrecioBase()

        if self.getInternacionales() > 10:
            importe += ((base*15)/100)
        return importe
    
