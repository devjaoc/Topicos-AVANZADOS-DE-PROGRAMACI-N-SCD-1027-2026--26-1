class Calculadora:
    __tipoCalculadoraNombre:str
    """ calculadora()  """

    def __init__(self,tipoCalculadora):
        print(tipoCalculadora)
        self.__tipoCalculadoraNombre=tipoCalculadora;
        
    def suma(self,a,b):#this self             
        self.__metodoInterno()     
        return a+b
    def __metodoInterno(self):
        pass
    def getTipo(self):
        return self.__tipoCalculadoraNombre;
    def set_tipoCalculadoraNombre(self,tipoCalculadoraNombre):
        self.__tipoCalculadoraNombre=tipoCalculadoraNombre
class Persona:
    def __init__(self):
        pass