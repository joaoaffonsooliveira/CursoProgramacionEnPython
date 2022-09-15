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

def color_menu(t):
	f="\033[0;37;40m"
	p="\033[1;33;41m"
	print(p+"\t"+t+f)

borra()	
# Declaramos una lista vacia
mi_lista = ["Argentina","Bolivia","Brasil","Ecuador"]
mi_lista2 = [1,2,3.1,"4","5.1","3.15",'"3.1"',"3,1","'3.1'"]
def menu_lista():
	borra()
	lm=["╔══════════════════╗",
		"║ Métodos de lista ║",
		"║                  ║",
		"║   1  append      ║",
		"║   2  clear       ║",
		"║   3  count       ║",
		"║   4  extend      ║",
		"║   5  index       ║",
		"║   6  insert      ║",
		"║   7  pop         ║",
		"║   8  remove      ║",
		"║   9  reverse     ║",
		"║  10  sort        ║",
		"║  11  muestra     ║",
		"║   S  sale        ║",
		"╚══════════════════╝"]
	l= len(lm)
	for i in range (l):
		color_menu(lm[i])	
	op=input("\tSeleccione opción: ")
	return op

# 1 append Agregar elementos en la lista
def agregar(lista):
	if (input("Ingresa numero(N) o palabra(P): ").upper())=="N":
		elem=float(input("   Ingrese un valor: "))
	else:
		elem=input("Ingrese una palabla: ")	
	# Y ahora si agregamos el elemento a la lista
	lista.append(elem)

# 2 clear Para limpiar una lista
def limpia_lista(lista):
	lista.clear()
	

# 3 count Veces que un elemento se encuentra en una lista
def cuenta(lista):
	#for i in range (len(lista)):
	#	print (lista[i], type(lista[i]))
	#tipo=input("""¿El elemento a buscar es:
	#	1...Un entero
	#	2...Un flotante
	#	3...Una cadena de caracteres
	#	4...Un valor lógico""")


	elem=input("Elemento a buscar: ")
	if elem.isnumeric():   
		el=int(elem)
	elif not(elem.isalnum()) and elem.isdigit():
		el=float(elem)
	else:
		el=elem	
	#print (el, type(el))	
	print ("El elemento {} se repite {} veces".format(el,lista.count(el)))	 
	input()

# 4 extend Extiende una lista con elementos de otra lista (elemento iterable)
def extiende_lista(lista):
	print ("extend agrega una lista a otra lista")
	l2=[]
	for i in range(5):
		h=input("Elemento nuevo: ")
		l2.append(h)
	print(l2)	
	lista.extend(l2)	
	

# 5 index encuentran la posición de un elemento
def busca_pos(lista):
	print ("""El método index devuelve la 
	posición de un elemento buscado""")
	print(lista)
	elem=input("Ingrese elemento a buscar: ")
	h=lista.index(elem)
	print ("Posición index: ",h)
	
		
# 6 insert inserta elementos en una lista en una posición dada	
def insertar_en_lista(lista):
	print ("Inserta un elemento en una lista en una posicion determinada")
	pos=int(input("Ingrese posición donde insertar: "))

	if (input("Ingresa numero(N) o palabra(P): ").upper())=="N":
		elem=int(input("   Ingrese un valor: "))
	else:
		elem=input("Ingrese una palabla: ")	
	# Y ahora si insertamos el elemento a la lista
	lista.insert(pos,elem)

# 7 pop borra el último elemento de la lista
def borra_ultimo(lista):
	lista.pop()

# 8 remove Remueve la primer aparición de un elemento de una lista
def borra_elemento(lista):
	bor=input("Ingrese elemento a borrar: ")
	lista.remove(bor)
	

# 9 reverse Revierte una lista
def revierte_lista(lista):
	lista.reverse()

# 10 sort Ordena lista
def ordena_lista(lista):
	lista.sort()
	
	
# 11 mustra lista
def recorre_lista(lista):
	largo=len(lista)
	if largo ==0:
		print ("La lista está vacía")
	else:	
		for i in range(largo):
			print (lista[i],end= " ")
	input("\nEsperando que toques una tecla...")			

while True:
	op=menu_lista()
	if op == "1":
		agregar(mi_lista)
		recorre_lista(mi_lista)
	elif op =="2":
		recorre_lista(mi_lista)
		limpia_lista(mi_lista)
		recorre_lista(mi_lista)
	elif op =="3":
		recorre_lista(mi_lista)
		cuenta(mi_lista)
	elif op =="4":
		recorre_lista(mi_lista)
		extiende_lista(mi_lista)
		recorre_lista(mi_lista)
	elif op =="5":
		recorre_lista(mi_lista)
		busca_pos(mi_lista)
	elif op =="6":
		recorre_lista(mi_lista)
		insertar_en_lista(mi_lista)
		recorre_lista(mi_lista)
	elif op =="7":
		recorre_lista(mi_lista)
		borra_ultimo(mi_lista)
		recorre_lista(mi_lista)
	elif op =="8":
		recorre_lista(mi_lista)
		borra_elemento(mi_lista)
		recorre_lista(mi_lista)
	elif op =="9":
		recorre_lista(mi_lista)
		revierte_lista(mi_lista)
		recorre_lista(mi_lista)
	elif op =="10":
		ordena_lista(mi_lista)
	elif op =="11":		
		recorre_lista(mi_lista)
	elif op.upper()=="S":
		break
