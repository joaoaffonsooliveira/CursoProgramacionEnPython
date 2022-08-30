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

system(s)

print (" Autor: "+f" {autor}".rjust(60,"-"))
print (" Fecha: "+f" {dia}/{mes}/{anio}".rjust(60,"-"))

print ("Solo podrán entrar menores hasta 10 y mayores de 70")
print ("Solo podran salir mayores de 10 y menores hasta 70")

print ("Solo podrán entrar menores hasta 10 o mayores de 70")
print ("Solo podran salir mayores de 10 o menores hasta 70")

print ("Solo podrán entrar menores hasta 10 y mayores de 70")
print ("Solo podran salir mayores de 10 o menores hasta 70")

print ("Solo podrán entrar menores hasta 10 o mayores de 70")
print ("Solo podran salir mayores de 10 y menores hasta 70")

edad= int(input("Ingresar edad: "))
donde= int (input ("Esta: \n1) Quiere entrar \n2) Quiere salir \nSeleccione opción: "))
"""
00,01,02,03,04,05,06,07,08,09,
10,

11,12,13,14,15,16,17,18,19,
20,21,22,23,24,25,26,27,28,29,
30,31,32,33,34,35,36,37,38,39,
40,41,42,43,44,45,46,47,48,49,
50,51,52,53,54,55,56,57,58,59,
60,61,62,63,64,65,66,67,68,69,
70,

71,72,73,74,75,76,77,78,79,
80,81,82,83,84,85,86,87,88,89,
90,91,92,93,94,95,96,97,98,99,
"""

if donde==1 and (edad<=10 or edad>70):
	print ("Puede ingresar")
elif donde==2 and (10<edad<=70):
	print ("Puede salir")
elif donde==1:
	print ("Solo puede ingresar si tiene hasta 10 años o es mayor de 70 años")
else:
	print ("Solo puede salir si es mayor de 10 años  y menor de 70 años")			
