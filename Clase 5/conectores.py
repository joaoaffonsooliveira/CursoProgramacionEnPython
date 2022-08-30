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
print ("Solo podran salir mayores de 10 o menores hasta 70")
edad= int(input("Ingresar edad: "))


if edad<=10 and edad>70:
	print ("1 Puede entrar")
else:
	print ("2 Puede salir")

if edad<=10 or edad>70:
	print ("3 Puede entrar")
else:
	print ("4 Puede salir")		