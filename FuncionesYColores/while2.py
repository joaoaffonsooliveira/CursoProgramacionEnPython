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

sigue=="s" 

while sigue.lower()=="s":
	nombre=   input("    Nombre: ")
	apellido= input("  Apellido: ")
	sigue=    input("Sigue(s/n): ")
	print("nombre: ", nombre, "apellido: ", apellido)