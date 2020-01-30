''' Uso de un solo bloque de instrucciones  '''

# comparación de números
edad = 10
if edad >= 18:
    print("Eres mayor de edad")

# comparación de cadenas
respuesta = input("Desea salir (S/N)?: ")
if respuesta.upper()=='S':
    print("Hasta otra!")

# subcadenas
texto = 'esternocleidomastoideo'
if 'cleido' in texto:
    print (texto, 'contiene "cleido"')
if texto.find('cleido') != 0:
    print (texto, 'contiene "cleido" y empieza en el caracter', texto.find('cleido'))

# En listas
lista = [1, 2, 3, 4, 5, 6, 5]
if 5 in lista:
    print("La lista tiene un 5")

if lista.count(5) > 0:
    print("La lista tiene ",lista.count(5), " cincos")



