# Vamos a hacer un redondeo con un decimal
dividendo = float(input("Introduzca el dividendo: "))
divisor = float(input("Introduzca el divisor: "))

# Round tiene 2 parámetros: el número a redondear y los decimales
resultado = round(dividendo / divisor, 1)

print ("El resultado es ", resultado)