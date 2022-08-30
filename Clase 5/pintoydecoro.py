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

p =    imput("Falta pintura(S/N): ")
q =    input("Falta un cuadro(S/N): ")
if p=="S" and q=="S"
	print ("Pinto y pongo un cuadro")
elif p!="S"
	print ("Pinto")
else:
	print ("Pongo un cuadro")

if p=="S" or q=="S"
	print ("Preguntar que hacer")
elif p!="S"
	print ("Pinto")
elif q!="S"
	print ("Pongo un cuadro")	
else:
	print ("Pongo un cuadro")				