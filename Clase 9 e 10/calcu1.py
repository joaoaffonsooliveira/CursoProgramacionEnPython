from os import system
from datetime import date
import platform

def borrarPantalla():
	sistemaOperacional = platform.system()
	if sistemaOperacional == "Linux":
		sistema = "clear"
	else:
		sistema = "cls"
	system(sistema)

def profile():
	autor="Joao Affonso"
	fecha = date.today()
	dia = fecha.day
	mes = fecha.month
	anio = fecha.year
	print(" Autor: "+f"{autor}".ljust(40, " ") + f"Fecha: {dia}/{mes}/{anio}")
	
def menucalc():
	print("\tOperación")
	print("\t+...Suma")
	print("\t-...Resta")
	print("\t*...Multiplicación")
	print("\t/...División")
	print("\tS...Salir")
	opcion = input("Seleccione opción: " )
	return opcion
		
def ingresa_valor():
	while True:
		valor = input("ingresar valor numérico: ")
		if valor.isnumeric():
			valor = int(valor)
			break
	return valor
		
def suma():
	numero1 = ingresa_valor()
	numero2 = ingresa_valor()
	print(f"{numero1} + {numero2} = {numero1 + numero2}")
	input(" ")
def resta():
	numero1 = ingresa_valor()
	numero2 = ingresa_valor()
	print(f"{numero1} - {numero2} = {numero1 - numero2}")
	input(" ")
def producto():
	numero1 = ingresa_valor()
	numero2 = ingresa_valor()
	print(f"{numero1} * {numero2} = {numero1 * numero2}")
	input(" ")
def division():
	numero1 = ingresa_valor()
	while True:
		numero2 = ingresa_valor()
		if numero2 != 0:
			break
	print(f"{numero1} / {numero2} = {numero1 / numero2}")
	input(" ")
while True:
	borrarPantalla()
	profile()
	oper=menucalc()
	
	if oper=="+":				suma()
	elif oper =="-":			resta()
	elif oper=="*":				producto()
	elif oper=="/":				division()
	elif oper.upper()=="S":		exit()				
	
