texto = input("Escribe un texto: ")

if texto.startswith('A'):
    print("El texto empieza por A")
elif texto.startswith('E'):
    print("El texto empieza por E")
elif texto.startswith('I'):
    print("El texto empieza por I")
else:
    print("El texto NO empieza por A, E ni I")