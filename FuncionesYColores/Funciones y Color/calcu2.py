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
		
def suma(a,b):
	print (f"{a} + {b} = {a+b}")
	
def resta(a,b):
	print (f"{a} - {b} = {a-b}")
	

def producto(a,b):
	print (f"{a} * {b} = {a*b}")
	

def division(a,b):
	while True:
		if b!=0:
			break
		else:
			b=ingresa_valor()	
	print (f"{a} / {b} = {a/b}")		
		

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