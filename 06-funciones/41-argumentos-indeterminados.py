# Función con un número indeterminado de parámetros
# Al final, lo que le llega a la función es una tupla
# con los valores pasados
def saludar_personas(*personas):
    print("Tupla de personas: ", personas)

    for persona in personas:
        print("Hola, ", persona)

def pintar_ficha_personal(**datos):
    print("Diccionario: ", datos)
    print("------------------------")
    print("Datos personales: ")
    print("------------------------")
    for dato in datos:
        print(dato, ": ",datos[dato])
    print("")

# Función con un número indeterminado de parámetros con nombre
# A la función le llega un diccionario con los parámetros.


# Invocamos a saludar_personas con distinto número de parámetros
saludar_personas("Jesús", "María", "Julián")
saludar_personas("Jesús")
saludar_personas("Jesús", "María", "Julián", "Ana", "Eva", "Leo")
saludar_personas(True, 12, 3.1, [1, 2, 3])


# Invocamos a función con un número indeterminado de parámetros con nombre
pintar_ficha_personal(dni='71823412', nombre='Sofía', apellidos='Esteban')
pintar_ficha_personal(nif='89123412', nombre='Manuel')