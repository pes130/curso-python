# Paso por posición
def division (dividendo, divisor):
	return dividendo / divisor

# Función con parémetros por defecto
def saludar (nombre='unnamed', apellidos='unsurnammed'):
    print("Hola: ")
    print("| Nombre:\t", nombre)
    print("| Apellidos:\t", apellidos)
    print("---------------------------")



# Llamamos a la función 'division', pasándole los parámetros por posición
print("3 / 2 es", division(3,2))
print("10 / 5 es", division(10,5))

# Llamamos a la función 'division', pasándole los parámetros por posición
print("Paso por nombre(1): 3 / 2 es", division(dividendo=3,divisor=2))
print("Paso por nombre(2): 3 / 2 es", division(divisor=2, dividendo=3))


# Llamamos a una función con parámetros por defecto
saludar("Juan")
saludar(apellidos="Madrigal")
saludar()