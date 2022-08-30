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
print (" Calculadora ".center(68,"*").upper())



a=int(input("Ingrese un valor: "))
b=int(input("Ingrese un valor: "))
c="No hay resultado"
print ("\tCalculadora")
print ("\t1 Suma")
print ("\t2 Resta")
print ("\t3 Producto")
print ("\t4 Cociente")
print ("\t5 Salir")

op=int(input("seleccione una opción: "))
if op == 1:		
	c=a+b
elif op == 2:	
	c=a-b
elif op == 3:	
	c=a*b
elif op == 4:
	if b!=0:
		c=a/b 	
	else:		
		print("No se puede dividir por 0")

print("El resultado es: ",c)

 















