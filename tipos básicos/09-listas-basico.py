# Declaración de una lista
# lista vacía
mi_lista = []

''' Creamos una lista con elementos. 
Los elementos pueden ser heterogéneos '''
mi_lista = ['Amparo', 12, 'Julio', 7.5, True]
print("Mi lista es: ", mi_lista)

# Acceso a elementos por index
print("Elemento 0:", mi_lista[0])
print("Elemento 4:", mi_lista[4])

# Longitud de una lista
print("La lista tiene ", len(mi_lista))

# Unión de listas
mi_lista_2 = ["Seat", False, ["CPU", "RAM", 12.1]]
lista_union = mi_lista + mi_lista_2
print("mi_lista: ", mi_lista)
print("mi_lista_2: ", mi_lista_2)
print("lista_union: ", lista_union)
