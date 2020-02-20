'''
    Solicita un número hasta que le pases cadena vacía

    El programa debe contar cuántos números has introducido,
    La suma de todos, y la media.

    Además, deberá guardarlos todos en una lista y mostrarlos
    al final en el mismo orden en que se introdujeron
'''
lista = []
entrada = "."
contador = 0
suma = 0


while entrada != "":
    entrada = input("Introduce un número. '' para salir: ")

    if entrada.isdigit():
        numero = int(entrada)
        contador+=1
        suma+=numero
        lista.append(numero)

print("Has metido", contador, "números")
print("La media es", suma/contador)
print("Los números son", lista)



