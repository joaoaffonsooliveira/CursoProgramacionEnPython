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


profile()	
lista=[]
def menu1():
	print ("\tMétodos de lista")
	print ("\t1...Agregar")
	print ("\t2...Insertar")
	print ("\t3...agregar varios")
	print ("\t4...Ver lista")
	print ("\tS...Salir")
	o = input ("Ingresar opción: ")
	return o

def menu2():
	print ("\tAgregar varios")
	print ("\t1...Como un unico elemento")
	print ("\t2...Como elementos individuales")
	print ("\tT...Terminar")
	td=input("Ingresar opción: ")
	return td

def agregar(li,t):
	li.append(t)



while True:
	borra()
	op=menu1()
	if op =="1":
		print ("Agregando elemento a la lista con el método append")
		elm= input ("ingresa nuevo elemento: ")
		agregar(lista,elm)
		
	if op =="2":
		print ("Insertar con el método insert")
		pos=int(input("Ingresar posición donde insertar: "))
		elem=input("Ingresar el elemento a  insertar: ")
		lista.insert(pos,elem)
	elif op =="3":
		while True:
			al=menu2()
			if al.upper()=="T":
				break
			print ("Carga una nueva lista:")
			nlista=[]
			while True:
				nel=input("Ingresar elemento (con enter se sale): ")
				if nel!="":
					agregar(nlista,nel)
				else:
					break				
			if al=="1":
				print ("Se grega un único elemento con append")
				lista.append(nlista)
			if al=="2":
				print ("Se agregan varios elemntos con extend")	
				lista.extend(nlista)
	elif op =="4":	
		input ("Ver lista")
		for i in range (len(lista)):
			print (i,lista[i])	
		input("...Proceso terminado...")	
	elif op.upper() =="S":
		exit()			

