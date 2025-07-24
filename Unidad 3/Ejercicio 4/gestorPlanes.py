import csv
from clasePlan import Plan
from planTelefonia import PlanTelefonia
from planTelevision import PlanTelevision

class GestorPlanes:
    __listaPlanes: list

    def __init__(self):
        self.__listaPlanes = []

    def agregarPlan(self, unPlan):
        self.__listaPlanes.append(unPlan)

    def cargarArchivo(self):
        archivo = open("planes.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader) 

        for fila in reader:
            if fila[0] == "M":
                plan = PlanTelefonia(fila[1], int(fila[2]), fila[3], int(fila[4]), fila[5], int(fila[6]))
            else:
                plan = PlanTelevision(fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), int(fila[6]))
            self.agregarPlan(plan)
            print("Plan cargado!")
        archivo.close()
    
    #Inciso 1
    def mostrarTipoPlan(self, pos):
        if 0 <= pos < len(self.__listaPlanes):
            plan = self.__listaPlanes[pos]
            if isinstance(plan, PlanTelefonia):
                print("El plan en la posicion", pos, "es de tipo Telefonia.")
            elif isinstance(plan, PlanTelevision):
                print("El plan en la posicion", pos, "es de tipo Television.")
            else:
                print("Tipo de plan desconocido.")
        else:
            raise IndexError
    
    #Inciso 2
    def cantidadPlanesCobertura(self, cobertura):
        contador = 0
        for plan in self.__listaPlanes:
            if plan.getCobertura().lower() == cobertura.lower():
                contador += 1
        return contador
    
    #Inciso 3
    def companiasPorCantidad(self, cantidad):
        print("Companias que ofrecen una cantidad de canales internacionales mayor o igual al valor ingresado: ")
        encontrado = False
        for plan in self.__listaPlanes:
            if isinstance(plan, PlanTelevision):
                if plan.getInternacionales() >= cantidad:
                    encontrado = True
                    print("Compañia:", plan.getCompania())
        
        if not encontrado:
            print("No se encontraron companias.")
    
    #Inciso 4
    def mostrarPlanes(self):
        i = 1
        for plan in self.__listaPlanes:
            print(f"Plan N°: {i}")
            if isinstance(plan, PlanTelefonia):
                print("Tipo de plan: Telefonia")
                print(f"Compania: {plan.getCompania()}")
                print(f"Duracion del plan: {plan.getDuracion()}")
                print(f"Cobertura geografica: {plan.getCobertura()}")
                print(f"Importe final: {plan.getImporteFinal()}")
            else:
                print("Tipo de plan: Television")
                print(f"Compania: {plan.getCompania()}")
                print(f"Duracion del plan: {plan.getDuracion()}")
                print(f"Cobertura geografica: {plan.getCobertura()}")
                print(f"Importe final: {plan.getImporteFinal()}")
            i += 1