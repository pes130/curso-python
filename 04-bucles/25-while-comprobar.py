'''
    Programa que te pide números hasta que introduzcas 
    un -1
'''
numero = 0

while numero != -1:
    numero = int(input("Dame un número (-1 para salir):"))
    print("Has introducido", numero)

print("Fin")