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

print ("Listas")
	
pais1=["Argentina","Bolivia","Brasil","Cuba","Ecuador"]
pais2=("Honduras","Paraguay","Peru","Uruguay","Venezuela")
print (pais1)
print (pais2)

print ()

b= len (pais1)
for i in range(b):
	print(pais2[i], end= " - ")
print ()
h=len(pais2)	

for i in range(h):
	print(pais2[i], end= " - ")
print()
