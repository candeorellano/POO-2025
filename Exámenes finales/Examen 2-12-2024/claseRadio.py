from claseMedio import Medio
from clasePrograma import Programa
from datetime import datetime

class Radio(Medio):
    __frecuencia:str
    __programas:list

    def __init__(self, nom, aud, frec):
        super().__init__(nom, aud)
        self.__frecuencia = frec
        self.__programas = []

    def getFrecuencia(self):
        return self.__frecuencia
    
    def agregaPrograma(self, nom, hi, hf):
        HI = datetime.strptime(hi, "%H:%M").time()
        HF = datetime.strptime(hf, "%H:%M").time()
        if HI < HF:
            self.__programas.append(Programa(nom, HI, HF)) #Composicion
        else:
            raise ValueError("La hora de inicio debe ser anterior a la hora de fin.")

    def __str__(self):
        return f"{super().__str__()}, Frecuencia: {self.getFrecuencia()}"
    
    def buscarPrograma(self, nombre):
        i = 0
        encontrado = False
        prog = None

        while i < len(self.__programas) and not encontrado:
            prog = self.__programas[i]
            if prog.getNombre().lower() == nombre.lower():
                encontrado = True
            else:
                i += 1
        return prog
    
    def cantidadProgramas(self):
        cantidad = len(self.__programas)
        return cantidad
    
    def indiceAudiencia(self):
        if self.cantidadProgramas() > 0:
            indice = self.getAudiencia() / self.cantidadProgramas()
        else:
            indice = 0
        return indice