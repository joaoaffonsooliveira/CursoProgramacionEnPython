from os import system
from datetime import date
import platform

def color(t):
	f=chr(27)+"[0;37;40m"
	bp()
	print ("\tEstilos        \tColores....Texto \t....Fondo")
	print ("\tSin efecto...0 \tNegro.......30   \t.....40")
	print ("\tNegrita......1 \tRojo........31   \t.....41")
	print ("\tDébil........2 \tVerde.......32   \t.....42")
	print ("\tCursiva......3 \tAmarillo....33   \t.....43")
	print ("\tSubrayado....4 \tAzul........34   \t.....44")
	print ("\tInverso......5 \tMorado......35   \t.....45")
	print ("\tOculto.......6 \tCian........36   \t.....46")
	print ("\tTachado......7 \tBlanco......37   \t.....47")
	est=input("\t        Seleccione estilo: ")
	cte=input("\tSeleccione color de texto: ")
	cfo=input("\tSeleccione color de fondo: ")
	k =chr(27)+f"[{est};{cte};{cfo}m"
	n=k+t+f
	return n



def bp():
	so= platform.system()
	if so=="Linux":
		s="clear"
	else:
		s="cls"
	system(s)

def profile():
	autor="ROHC"
	fc = date.today()
	dia=fc.day
	mes=fc.month
	anio=fc.year
	print (" Autor: "+f"{autor}".ljust(40," ")+f"Fecha: {dia}/{mes}/{anio}")
	
def menucalc():
	print (chr(27)+"[1;33m"+"\tOperación"+chr(27)+"[1;37m")
	print (chr(27)+"[1;32m"+"\t+...Suma")
	print ("\t-...Resta")
	print ("\t*...Multiplicación")
	print ("\t/...División")
	print ("\tS...Salir"+chr(27)+"[1;37m")
	op= input("Seleccione opción: " )
	return op
		
def ingresa_valor():
	while True:
		val=input("ingresar valor numérico: ")
		if val.isnumeric():
			val=int(val)
			break
	return val	
		
def suma(a,b):
	r=color(str(n+b))
	print (f"{a} + {b} = {r}")
	
def resta(a,b):
	r=color(str(n-b))
	print (f"{a} - {b} = {r}")
	

def producto(a,b):
	r=color(str(n*b))
	print (f"{a} * {b} = {r}")
	

def division(a,b):
	
	while True:
		if b!=0:
			break
		else:
			b=ingresa_valor()
	r=color(str(n/b))
	print (f"{a} / {b} = {r}")		
		

while True:
	bp()
	profile()

	oper=menucalc()
	if oper.upper()=="S":
		exit()

	n=ingresa_valor()
	m=ingresa_valor()

	if oper=="+":				
		suma(n,m)
	elif oper =="-":
		resta(n,m)
	elif oper=="*":				
		producto(n,m)
	elif oper=="/":				
		division(n,m)
	input("")	