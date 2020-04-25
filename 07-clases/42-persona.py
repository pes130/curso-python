from datetime import datetime

class Persona:

    def __init__(self, nombre, apellidos, dni, anyo_nac):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.anyo_nacimiento = anyo_nac
    
    def devolver_edad(self):
        anyo_actual = datetime.today().year
        return anyo_actual - self.anyo_nacimiento
    
    def incrementar_anyo_nacimiento(self, incremento):
        self.anyo_nacimiento+= incremento
    

persona1 = Persona('John', 'Connor', '61723456P', 1976)
print(persona1.nombre)
print(persona1.anyo_nacimiento)

print(persona1.devolver_edad())
persona1.incrementar_anyo_nacimiento(3)
print(persona1.devolver_edad())



