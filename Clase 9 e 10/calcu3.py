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
	print ("\tOperación: +, -, *, /")
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
		
def suma(a):
	b=ingresa_valor()
	print (f"{a} + {b} = {a+b}")
	
def resta(a):
	b=ingresa_valor()
	print (f"{a} - {b} = {a-b}")
	

def producto(a):
	b=ingresa_valor()
	print (f"{a} * {b} = {a*b}")
	

def division(a):
	while True:
		b=ingresa_valor()
		if b!=0:
			break
	print (f"{a} / {b} = {a/b}")		
		

while True:
	bp()
	profile()
	n=ingresa_valor()
	
	oper=menucalc()
	if oper.upper()=="S":
		exit()

	if oper=="+":				
		suma(n)
	elif oper =="-":
		resta(n)
	elif oper=="*":				
		producto(n)
	elif oper=="/":				
		division(n)
	input("")	