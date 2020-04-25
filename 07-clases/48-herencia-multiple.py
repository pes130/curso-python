from datetime import datetime
import uuid

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

class Cyborg:

    def __init__(self, modelo):
        self.modelo = modelo
        self.serie = uuid.uuid4()

    def devolver_numero_serie(self):
        return self.serie

    def presentar(self):
        print("Modelo: {} Serie: {}".format(
            self.modelo, self.serie
        ))
    


class CyborgBueno(Resistencia, Cyborg):

    def __init__(self, modelo, nombre, anyo_nacimiento, alias, faccion):
        Cyborg.__init__(self, modelo)
        Resistencia.__init__(self, nombre, None, anyo_nacimiento, alias, faccion)

    

t1000 = Cyborg('t-1000')
print(t1000.devolver_numero_serie())

t800 = CyborgBueno('t800', 'Carl', 2020, 'El abuelo', 'Hollywod')
t800.presentar()




