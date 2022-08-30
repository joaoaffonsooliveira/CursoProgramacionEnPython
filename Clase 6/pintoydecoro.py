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
print (" Fecha: "+f" {dia}/{mes}/{anio}".rjust(66,"-"))

p =    input("  Falta pintura(S/N): ")
q =    input("Falta un cuadro(S/N): ")

if p.upper()=="S" and q.upper()=="S":	
	print ("Pinto y pongo un cuadro")
elif p.upper() =="S":					
	print ("Pinto")
elif q.upper()=="S":					
	print ("Pongo un cuadro")
else:									
	print ("No hacer nada")

print ("***Segunda forma***")
if p.upper()=="S":		
	print("Pinto")
	if q.upper()=="S":	
		print ("Pongo un cuadro")
elif q.upper()=="S":	
	print ("Pongo un cuadro")
else:					
	print ("No hacer nada")
		