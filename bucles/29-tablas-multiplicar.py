''' 
    Calcula la tabla de multiplicar de un 
    número dado
    Ej. Si le paso 7:
    7 x 0 = 0
    7 x 1 = 7
    7 x 2 = 14
    ...
    7 x 10 = 70
    Hazlo con un for
'''
entrada = input("Escribe un número:")

if entrada.isdigit():
    numero = int(entrada)

    for contador in range(11):
        print(numero, "x",contador,"=",numero*contador)









