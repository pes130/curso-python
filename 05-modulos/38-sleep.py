from random import randint
from time import sleep, strftime, localtime

for n in range(10):
    numero=randint(1,100)
    print('Generación:',n+1,'Número generado:',numero,'hora: ',strftime('%H:%M:%S', localtime()))
    sleep(1)