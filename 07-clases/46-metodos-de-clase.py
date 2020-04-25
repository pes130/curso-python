from datetime import datetime

class Persona:
    __contador = 0

    def __init__(self, nombre, apellidos, dni, anyo_nac):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__anyo_nacimiento = anyo_nac
        Persona.__contador+=1
    
    def devolver_edad(self):
        anyo_actual = datetime.today().year
        return anyo_actual - self.__anyo_nacimiento
    
    def incrementar_anyo_nacimiento(self, incremento):
        self.__anyo_nacimiento+= incremento

    @staticmethod
    def devolver_contador():
        return Persona.__contador

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        self.__dni = dni


    @property
    def edad(self):
        return self.devolver_edad()

    @edad.setter
    def edad(self, edad):
        anyo_nacimiento = datetime.today().year - edad
        self.__anyo_nacimiento = anyo_nacimiento

    
    

persona1 = Persona('John', 'Connor', '61723456P', 1976)
print(Persona.devolver_contador())

persona2 = Persona('John', 'Connor', '61723456P', 1976)
print(Persona.devolver_contador())

persona3 = Persona('John', 'Connor', '61723456P', 1976)
print(Persona.devolver_contador())
