''' Uso de un solo bloque de instrucciones  '''

# comparación de números
edad = 10
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# comparación de cadenas
respuesta = input("Desea salir (S/N)?: ")
if respuesta.upper()=='S':
    print("Hasta otra!")
else:
    print("Pues aquí seguimos")

# subcadenas
texto = 'esternocleidomastoideo'
if 'cleido' in texto:
    print (texto, 'contiene "cleido"')
else:
    print (texto, ' NO contiene "cleido"')

if texto.find('cleido') != 0:
    print (texto, 'contiene "cleido" y empieza en el caracter', texto.find('cleido'))
else:
    print (texto, 'contiene "cleido"')

# En listas
lista = [1, 2, 3, 4, 5, 6, 5]
if 5 in lista:
    print("La lista tiene un 5")
else:
    print("La lista NO tiene un 5")




