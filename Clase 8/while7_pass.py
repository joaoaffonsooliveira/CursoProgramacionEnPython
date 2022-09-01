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

a=20
while not True:
	
print("No usar pass da un error el bucle no puede estar vacío")