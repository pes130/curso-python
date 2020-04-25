from datetime import datetime

class Persona:
    contador = 0

    def __init__(self, nombre, apellidos, dni, anyo_nac):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__anyo_nacimiento = anyo_nac
        Persona.contador+=1
    
    def devolver_edad(self):
        anyo_actual = datetime.today().year
        return anyo_actual - self.__anyo_nacimiento
    
    def incrementar_anyo_nacimiento(self, incremento):
        self.__anyo_nacimiento+= incremento
    

persona1 = Persona('John', 'Connor', '61723456P', 1976)
print(persona1.__nombre)






