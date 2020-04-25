from datetime import datetime

class Persona:
    contador = 0

    def __init__(self, nombre, apellidos, dni, anyo_nac):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.anyo_nacimiento = anyo_nac
        Persona.contador+=1
    
    def devolver_edad(self):
        anyo_actual = datetime.today().year
        return anyo_actual - self.anyo_nacimiento
    
    def incrementar_anyo_nacimiento(self, incremento):
        self.anyo_nacimiento+= incremento
    

persona1 = Persona('John', 'Connor', '61723456P', 1976)
print("Total personas:", Persona.contador)

persona2 = Persona('Sarah', 'Connor', '45723456P', 1951)
print("Total personas:", Persona.contador)

persona3 = Persona('Kyle', 'Reese', '75723456P', 2010)
print("Total personas:", Persona.contador)
print("Total personas:", persona3.contador)






