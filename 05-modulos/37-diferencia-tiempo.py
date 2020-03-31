from time import time

tiempo1=time()
palabra=input('Escribe una palabra y pulsa intro: ')
tiempo2=time()
diferencia=tiempo2-tiempo1
print('has tardado',diferencia,'segundos en escribir la palabra',palabra)