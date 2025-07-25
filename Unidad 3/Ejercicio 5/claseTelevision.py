from claseMedio import Medio
from clasePrograma import Programa

class Television(Medio):
    __canales:int
    __canal:str
    __programas:list

    def __init__(self, nom, aud, cant, canal):
        super().__init__(nom, aud)
        self.__canales = cant
        self.__canal = canal
        self.__programas = []

    def getCantidadCanales(self):
        return self.__canales
    
    def agregaPrograma(self, unPrograma):
        if isinstance(unPrograma, Programa):
            self.__programas.append(unPrograma)
        else:
            raise TypeError("El objeto debe ser una instancia de Programa")
        
    def __str__(self):
       return f"{super().__str__()}, Cantidad de Canales: {self.__canales}, Canal: {self.__canal}"

    def buscarPrograma(self, nombre):
        encontrado = False
        retorno = None
        i = 0
        while i < len(self.__programas) and not encontrado:
            if self.__programas[i].getNombre().lower() == nombre.lower():
                retorno = self.__programas[i]
                encontrado = True
            else:
                i += 1
        return retorno
    
    def muestraProgramacion(self):
        print(f"  Programación del canal {self.__canal}:")
        if not self.__programas:
            print("    (Sin programas)")
        for p in self.__programas:
            print(f"    - {p}")
