# Vamos a hacer un redondeo con un decimal
dividendo = float(input("Introduzca el dividendo: "))
divisor = float(input("Introduzca el divisor: "))
redondeo = int(input("¿Cuántos decimales quieres redondear?"))

# Round tiene 2 parámetros: el número a redondear y los decimales
resultado = round(dividendo / divisor, redondeo)

print ("El resultado es ", resultado)