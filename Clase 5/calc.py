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
n1=int(input("  Ingresar 1º número: "))
n2=int(input("  Ingresar 2º número: "))
suma =n1 + n2
print (f"                Suma: {suma}")
resta=n1 - n2
print (f"          Diferencia: {resta}")
prod =n1 * n2
print (f"            Producto: {prod}")
dive =n1 //n2
print (f"     Cociente entero: {dive}")
rsdiv=n1 % n2
print (f"Resto de la división: {rsdiv}")

# ************************************************
divr =n1 / n2
print (f"       Cociente real: {divr:.3f}")
print (f"       Cociente real: {round(divr,3)}" )

# *************************************************
poten=n1**n2
print (f" {n1} elevado a {n2}: {poten}")
raiz =n1**(1/n2)
print (f"Raiz {n2} de {n1} es: {raiz:.5f}")
print (f"Raiz {n2} de {n1} es: {round(raiz,2)}")