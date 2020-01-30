resultado1 = True
resultado2 = False

print("resultado1: ", resultado1)
print("resultado2: ", resultado2)

# operadores lógicos
print("resultado1 and resultado2: ",resultado1 and resultado2)
print("resultado1 or resultado2: ",resultado1 or resultado2)
print("not resultado1: ", not resultado1)

# Tabla AND
print("Operador 1\tOperador2\tResultado")
print("-------------------------------------------")
print(False, "\t\t", False, "\t\t", False and False)
print(False, "\t\t", True, "\t\t", False and True)
print(True, "\t\t", False, "\t\t", True and False)
print(True, "\t\t", True, "\t\t", True and True)

# Tabla OR
print("Operador 1\tOperador2\tResultado")
print("-------------------------------------------")
print(False, "\t\t", False, "\t\t", False or False)
print(False, "\t\t", True, "\t\t", False or True)
print(True, "\t\t", False, "\t\t", True or False)
print(True, "\t\t", True, "\t\t", True or True)
