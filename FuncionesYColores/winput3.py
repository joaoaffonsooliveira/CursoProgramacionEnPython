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

# input en Python, uso de set y del operador walrus
print (" 1ra forma ".center(30,"*"))
print("Buscamos en el numero: 123456")

while (n:=input("Ingresar numero: ")) in ("123456"):	

	print(f'El numero {n} está en el conjunto ("123456")')
print (f"Saliste del ciclo porque {n}, no está en (123456)")
input("...")

system(s)

# input en Python, uso de set y del operador walrus y objeto iterable
# para que sea iterable usar "," al final
print (" 2ra forma ".center(30,"*"))
print("Buscamos en el numero: 123456")
while (n:=int(input("Ingresar numero: "))) in (123456):    

    print(f'El numero {n} está en el conjunto (123456)')
print (f"Saliste del ciclo porque {n}, no está en (123456)")
input("...")




