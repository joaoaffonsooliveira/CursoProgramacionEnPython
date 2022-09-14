from os import system 
from datetime import date
import platform


def borra():
	so=platform.system()
	if so=="Linux": 
		s="clear"
	else: 
		s="cls"
	system(s)	
		
def profile():
	autor="ROHC"
	hoy=date.today()
	fecha =[hoy,hoy.day,hoy.month,hoy.year]
	print (" Autor: "+f" {autor}"+f" {fecha[1]}/{fecha[2]}/{fecha[3]}".rjust(60,"-"))

borra()
profile()	
lista=[]

while True:
	borra()
	print ("\tMétodos de lista")
	print ("\t1...Agregar")
	print ("\t2...Insertar")
	print ("\t3...agregar varios")
	print ("\t4...Ver lista")
	print ("\tS...Salir")
	op = input ("Ingresar opción: ")
	if op =="1":
		print ("Agregando elemento a la lista con el método append")
		elm= input ("ingresa nuevo elemento: ")
		lista.append(elm)
	if op =="2":
		print ("Insertar con el método insert")
		pos=int(input("Ingresar posición donde insertar: "))
		elem=input("Ingresar el elemento a  insertar: ")
		lista.insert(pos,elem)
	if op =="3":
		while True:
			print ("\tAgregar avios")
			print ("\t1...Como un unico elemento")
			print ("\t2...Como elementos individuales")
			print ("\tT...Terminar")
			al=input("Ingresar opción: ")
			if al.upper()=="T":
				break
			print ("Carga una nueva lista:")
			nlista=[]
			while True:
				nel=input("Ingresar elemento (con enter se sale): ")
				if nel!="":
					nlista.append(nel)
				else:
					break				
			if al=="1":
				print ("Se grega un único elemento con append")
				lista.append(nlista)
			if al=="2":
				print ("Se agregan varios elemntos con extend")	
				lista.extend(nlista)
	elif op=="4":
		for i in range(len(lista)):
			print (lista[i])
	elif op.upper()=="S":
		exit()		
