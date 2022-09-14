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

def titulos():
	print ()
	f="\033[0;37;40m"
	t="\tLista Original".ljust(18,' ')+"Lista Inversa".ljust(17,' ')+"Lista Ordenada"
	p="\033[1;33;41m"
	print(p+t+f)

def direccion():
	print (f"""\033[1;33m\tDirección lista1: {id(lista1)}
\tDirección lista2: {id(lista2)}
\tDirección lista3: {id(lista3)}\033[0;37m""")	

borra()
profile()	
lista1=["Cuba","Ecuador","Argenina","Bolivia","Brasil", "Perú"]	
lista2=[]
lista3=[]
lista2.extend(lista1)
lista3.extend(lista1)
lista2.reverse()
lista3.sort()

direccion()
titulos()
for i in range(6):
	print (f"\t{lista1[i].ljust(15,' ')}  {lista2[i].ljust(16,' ')} {lista3[i]}")
