from os import system
from datetime import date
import platform

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
	print ("\tOperación")
	print ("\t+...Suma")
	print ("\t-...Resta")
	print ("\t*...Multiplicación")
	print ("\t/...División")
	print ("\tS...Salir")
	op= input("Seleccione opción: " )
	return op
		
def ingresa_valor():
	while True:
		val=input("ingresar valor numérico: ")
		if val.isnumeric():
			val=int(val)
			break
	return val	
		
def suma():
	a=ingresa_valor()
	b=ingresa_valor()
	print (f"{a} + {b} = {a+b}")
	input (" ")
def resta():
	a=ingresa_valor()
	b=ingresa_valor()
	print (f"{a} - {b} = {a-b}")
	input (" ")	
def producto():
	a=ingresa_valor()
	b=ingresa_valor()
	print (f"{a} * {b} = {a*b}")
	input (" ")
def division():
	a=ingresa_valor()
	while Tru:
		b=ingresa_valor()
		if b!=0:
			break
	print (f"{a} / {b} = {a/b}")		
	input (" ")		
while True:
	bp()
	profile()
	oper=menucalc()
	
	if oper=="+":				suma()
	elif oper =="-":			resta()
	elif oper=="*":				producto()
	elif oper=="/":				division()
	elif oper.upper()=="S":		exit()				
	
