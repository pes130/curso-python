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
print("Nombre:", persona1.nombre)
print("Apellidos:", persona1.apellidos)
print("DNI:", persona1.dni)
print("Edad:", persona1.edad)

persona1.nombre = 'Sarah'
persona1.apellidos = 'Connor'
persona1.dni = '34913758F'
persona1.edad = 38


print("Nombre:", persona1.nombre)
print("Apellidos:", persona1.apellidos)
print("DNI:", persona1.dni)
print("Edad:", persona1.edad)








