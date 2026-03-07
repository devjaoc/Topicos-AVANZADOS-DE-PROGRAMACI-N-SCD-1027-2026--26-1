from Calculadora import Calculadora
 
objCalculadora=Calculadora("Basica")    #obj=new Calculadora(); obj.suma(12,2);
print("Resultado "+str(objCalculadora.suma(12,2)))
print("Tipo "+objCalculadora.getTipo())
#print("Tipo "+objCalculadora.__tipoCalculadoraNombre)
objCalculadora.set_tipoCalculadoraNombre("Cientifica");
print("Tipo "+objCalculadora.getTipo())
#print("Metodo interno "+objCalculadora.__metodoInterno())