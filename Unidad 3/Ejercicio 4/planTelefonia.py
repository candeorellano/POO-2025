from clasePlan import Plan

class PlanTelefonia(Plan):
    __tipo:str
    __minutos:int

    def __init__(self, comp, dur, cob, pb, tipo, minutos):
        super().__init__(comp, dur, cob, pb)
        self.__tipo = tipo
        self.__minutos = minutos
    
    def getTipo(self):
        return self.__tipo
    
    def getMinutos(self):
        return self.__minutos
    
    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.__tipo}, Minutos incluidos: {self.__minutos}"
    
    def getImporteFinal(self):
        base = self.getPrecioBase()
        importe = self.getPrecioBase()

        if self.getTipo() == "internacional":
            importe += ((base*20)/100)
        elif self.getTipo() == "locales":
            importe -= ((base*7.5)/100)
        return importe

