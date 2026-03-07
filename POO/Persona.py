class Persona:
    nombre:str
    apellido:str 
    def hablar(self):
        print("Solo Persona")
    
class Alumno(Persona): #extens
    def hablar(self):
        print("Soy Alumno")
class Maestro(Persona):
    def hablar(self):
        print("Soy Maestro")
def hablar(persona):
    persona.hablar()
            
alumno=Alumno()
maestro=Maestro()
#print(alumno.hablar())
hablar(alumno)
hablar(maestro)