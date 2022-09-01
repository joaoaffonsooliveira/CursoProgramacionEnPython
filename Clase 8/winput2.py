#!/usr/bin/python3.8
from os import system 
from datetime import date
from random import choice
import platform
autor="ROHC"

# Guardamos el sistema operativo del systema
so=platform.system()
if so=="Linux":
  s="clear"
else:
  s="cls"
    
# Guardamos la fecha con dia, mes y año
hoy =date.today()
dia =hoy.day
mes =hoy.month
anio=hoy.year
system(s)

print (f" Autor: {autor}"+f" {dia}/{mes}/{anio}".rjust(40," "))

#input en Python, uso de set y del operador walrus

print (" 1ra forma ".center(30,"*"))
while (n:=int(input("Ingresar numero: "))) in (1,2,3,4,5,6):	

	print(f'El numero {n} está en el conjunto (1,2,3,4,5,6)')

print (f"Saliste del ciclo porque {n}, no está en el conjunto (1,2,3,4,5,6)")
input("...")

system(s)
print (" 2ra forma ".center(30,"*"))
#input en Python, uso de set y del operador walrus
while (n:=input("Ingresar numero: ")) in ("1","2","3","4","5","6"):    

    print(f'El numero {n} está en el conjunto ("1","2","3","4","5","6")')

print (f'Saliste del ciclo porque {n}, no está en el conjunto ("1","2","3","4","5","6")')
input("...")


system(s)
print (" 3ra forma ".center(30,"*"))
#input en Python, uso de set y del operador walrus
while (n:=input("Ingresar numero: ")) in ("1","2","3","4","5","6",1,2,3,4,5,6):    

    print(f"Tu ingreso fue: {n}")
    if (input("¿Es un nÚmero(S/N)?: ")).upper()=="S":
        nn=int(n)
        print (f'''Ingresaste el numero {nn} y está en conjunto
         ("1","2","3","4","5","6",1,2,3,4,5,6)''')
    else:
        print (f'''Ingresaste la letra {n} y está en conjunto
         ("1","2","3","4","5","6",1,2,3,4,5,6)''')    


print (f'''Saliste del ciclo porque {n}, no esta en el conjunto
    ("1","2","3","4","5","6",1,2,3,4,5,6)''')     