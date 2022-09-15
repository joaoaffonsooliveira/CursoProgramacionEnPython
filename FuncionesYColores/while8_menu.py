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

while True:
	print ("\tTiramos un título")
	print (" 1...Opción")
	print (" 2...Opción")
	print (" 3...Opción")
	print (" 4...Opción")
	print (" n...Opción")
	op=int(input("Seleccionar de 1 a 4: "))
	if op =="1":
		print("Ejecutamos opción 1")
	elif op =="2":
		print("Ejecutamos opción 2")
	elif op =="3":
		print("Ejecutamos opción 3")
	elif op =="4":
		print("Ejecutamos opción 4")

	elif op =="n":
		input ("Salimos del ciclo")
		exit()		
