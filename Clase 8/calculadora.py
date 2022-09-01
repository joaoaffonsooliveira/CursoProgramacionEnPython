from os import system
import platform
from datetime import date



while True:
	
	print ("Calculadora")
	print ("\t+...Suma")
	print ("\t-...Diferencia")
	print ("\t*...Producto")
	print ("\t/...Cociente")
	print ("\tS...Salir")

	if (op:=input("Ingresar operación: "))=="+":
		print ("Suma")
	elif op=="-":
		print ("Diferencia")
	elif op=="*":
		print ("Productos")
	elif op=="/":
		print ("División real")
	elif op.upper=="S":
		exit()				
