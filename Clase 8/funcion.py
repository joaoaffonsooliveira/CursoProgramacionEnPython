from os import system
from datetime import date
import platform
print ("""Una función en python es una estructura de codigo que se define con:
	def nombre_de_funcion (argumentos):
		cuerpo de la fución
		return valor de retorno""")
print ("Uso de la funcion: nombre_de_funcion(argumentos)")

# función borra pantalla

def bp():
	so=platform.system()
	if so=="Linux":
		s="clear"
	else:
		s="cls"
	system(s)
bp()	
print ("""Una función en python es una estructura de codigo que se define con:
def nombre_de_funcion (argumentos):
	cuerpo de la fución
	return valor de retorno""")
print ("Uso de la funcion: nombre_de_funcion(argumentos)")		

