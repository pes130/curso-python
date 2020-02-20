mi_lista = ['Amparo', 12, 'Julio', 7.5, True]
print("Lista original: ", mi_lista)

# LAs listas son de clase list.
print(mi_lista.__class__)

# Añadir un elemento: 2 posibilidades
# 1. Añadirlo al final de la lista: append(elemento)
mi_lista.append('Hola')
print('Lista tras añadir algo al final:', mi_lista)
# 2. Añadirlo a una posición específica: insert(index, elemento)
mi_lista.insert(3, 'zapatilla') #o sea , posición 4
print(mi_lista)

# Modificar un elemento: acceder a él y cambiarlo
mi_lista[4] = 'Uranio'
print(mi_lista)

# Eliminar elementos: 2 posibilidades
#1. Eliminamos por valor.
mi_lista.remove('Julio')
print(mi_lista)
# Y si tenemos varios elementos iguales?
mi_lista.insert(3, 'plomo')
mi_lista.insert(5, 'plomo')
mi_lista.insert(7, 'plomo')
# quita la primera ocurrencia
mi_lista.remove('plomo')
print(mi_lista)

# 2. Quitamos un elemento según su posición
# Borramos el elemento de índice 5, y lo guardamos en una variable
elemento_borrado = mi_lista.pop(6)
print(mi_lista)
print(elemento_borrado)

