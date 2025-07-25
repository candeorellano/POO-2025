from claseMedio import Medio
from clasePrograma import Programa

class Radio(Medio):
    __emisora:str
    __frecuencia:str
    __programas:list

    def __init__(self, nom, aud, emisora, frecuencia):
        super().__init__(nom, aud)
        self.__emisora = emisora
        self.__frecuencia = frecuencia
        self.__programas = []
    
    def getEmisora(self):
        return self.__emisora
    
    def getFrecuencia(self):
        return self.__frecuencia
    
    def agregaPrograma(self, unPrograma):
        if isinstance(unPrograma, Programa):
            self.__programas.append(unPrograma)
        else:
            raise TypeError("El objeto debe ser una instancia de Programa")
    
    def __str__(self):
        return f"{super().__str__()}, Emisora: {self.__emisora}, Frecuencia: {self.__frecuencia}"
    
    def muestraProgramacion(self):
        print(f"  Programación de {self.getEmisora()}:")
        if not self.__programas:
            print("    (Sin programas)")
        for p in self.__programas:
            print(f"    - {p}")
