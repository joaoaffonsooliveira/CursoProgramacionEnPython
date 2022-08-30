from os import system 
from datetime import date
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

"""
123
132
213
231
312
321
"""

system(s)
print ("Ordenar 3 números de mayor a menos")
a=int(input("Ingresar 1er numero:"))
b=int(input("Ingresar 2do numero:"))
c=int(input("Ingresar 3er numero:"))
if a>=b and a>=c:
	if b>c:
		pri=a
		seg=b 
		ter=c
	else:
		pri=a
		seg=c
		ter=b
elif b>=a and b>=c:
	if a>c:
		pri=b
		seg=a 
		ter=c
	else:
		pri=b
		seg=c 
		ter=a
elif a>b:
	pri=c
	seg=a
	ter=b
else:	
	pri=c 
	seg=b
	ter=a
print (f"El primero número es {pri}")
print (f"El segundo número es {seg}")
print (f"El  tercer número es {ter}")