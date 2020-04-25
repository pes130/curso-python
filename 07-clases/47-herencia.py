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

    def presentar(self):
        print("Nombre: {} Apellidos: {} Edad: {}".format(
            self.nombre, self.apellidos, self.devolver_edad()
    ))

class Resistencia(Persona):
    def __init__(self, nombre, apellidos, anyo_nacimiento, alias, faccion):
        super().__init__(nombre, apellidos, None, anyo_nacimiento)
        self.alias = alias
        self.faccion = faccion

    def presentar(self):
        super().presentar()
        print("Alias: {} Faccion: {}".format(
            self.alias, self.faccion
        ))
    

persona1 = Resistencia('John', 'Connor', 1976, "Lider de la Resitencia", "Washington DC")
persona1.presentar()






