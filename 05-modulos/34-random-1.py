import random

print('Programa para generar algunos datos aleatorios')
v1=random.random()
print('Valor aleatorio entre 0 y 1:',v1)
v2=random.randint(10,100)
print('Valor entero aleatorio entre 10 y 100:',v2)
v3=random.uniform(10,20)
print('Valor decimal entre 10 y 20:',v3)
nombres=['Ana','Julio','Dani','Aurora','Roberto','Martina','Hugo']
nom=random.choice(nombres)
print('El nombre elegido es:',nom)