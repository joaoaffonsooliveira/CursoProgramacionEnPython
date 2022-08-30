from os import system
from datetime import date
autor = "ROHC"
tema  = "Cadena de carateres"
hoy   = date.today()

# ******************************************************* 
system("clear")
print ("...ljust...")
cad="Python es un lenguaje de programación"
print (cad)
print ("ljust: Ubica una cadena de caracteres a la izquierda en un espacio prefijado")
print ("cad.ljust(espacio,relleno)")
print (cad.ljust(120,"*"))
input("...Fin ljust...")

# ******************************************************* 
system("clear")
print ("...rjust...")
cad="Python es un lenguaje de programación"
print (cad)
print ("rjust: Ubica una cadena de caracteres a la derecha en un espacio prefijado")
print ("cad.rjust(espacio,relleno)")
print (cad.rjust(60,"*"))
input("...Fin rjust...")

# ******************************************************* 
system("clear")
print ("...center...")
cad="Python es un lenguaje de programación"
print (cad)
print ("center: Ubica una cadena de caracteres al cedntro de un espacio prefijado")
print ("cad.center(espacio,relleno)")
print (cad.center(60,"*"))
input("...Fin center..")





