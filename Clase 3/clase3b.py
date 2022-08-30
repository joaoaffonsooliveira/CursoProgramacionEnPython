from os import system
from datetime import date
autor = "ROHC"
tema  = "Cadena de carateres"
hoy   = date.today()
cadena='''
Python pertenece al grupo de lenguajes de programación de alto nivel y orientados
a objetos, con una semántica dinámica integrada, principalmente para el desarrollo
web y de aplicaciones informáticas.
Es muy atractivo en el campo del Desarrollo Rápido de Aplicaciones (RAD) porque 
ofrece tipificación dinámica Python es simple y fácil de aprender, con una sintaxis 
única que se centra en la legibilidad. 
Los desarrolladores pueden leer y traducir el código Python mucho más fácil que con 
otros lenguajes.
Por tanto, esto reduce el costo de mantenimiento y de desarrollo del programa porque 
permite que los equipos trabajen en colaboración sin barreras significativas de 
lenguajes y experimentación.
Además, soporta el uso de módulos y paquetes, lo que significa que el programa Python
puede ser diseñado en con un estilo modular y su código puede ser reutilizado en 
varios proyectos. Una vez desarrollado un módulo o paquete, se puede escalar para su 
uso en otros proyectos, y es fácil de importar o exportar.
'''
# *******************************************************
system("clear")
print (autor.ljust(45," "), end=" ") # ajusta el texto a la izquierda
print (str(hoy).rjust(45," ")) # ajusta el texto a la derecha
print ("Funciones de cadena")
print (cadena)
largo=len(cadena)
print (f"Largo de la cadena: {largo}")
print ("Largo de la cadena: ",largo)
print ("Largo de la cadena: "+ str(largo))
input("...Esperame...")

# *******************************************************
system("clear")
print ("...count...")
print ("count     : Cuenta las veces que una cadena aparece en otra")
print ("cadena.count(subcadena, principio , fin)")
sc=input ("Ingresar subcadena: ")
p=int(input("Posicion donde comenzar la búsqueda: "))
f=int(input("Posición donde terminar la búsqueda: "))
print (f"La subcadena {sc} aparece {cadena.count(sc,p,f)} veces")
input ("...Fin count...")

# ******************************************************* 
system("clear")
print ("...find...")
print ("find: Muestra donde comienza una subcadena en otra, si no está devuelve -1")
sc=input("Cadena a buscar: ") 
p=int(input("  Valor inicial: "))
f=int(input("    Valor final: "))
print (f"La subcadena {sc} se encuentra en la posicion {cadena.find(sc,p,f)}")
input ("...Fin find...")

# ******************************************************* 
system("clear")
print ("...replace...")
cad="Python pertenece al grupo de lenguajes de programación de alto nivel orientado a objetos"
print (cad)
print ("replace: Reemplaza una subcadena con otra subcadena")
cadv=input("Qué parte de la oración desea reemplazar: ")
cadn=input("       Con que cadena desea reemplazarla: ")
rcad=cad.replace(cadv,cadn)

print(cad)
print (rcad)
# ***************************************
cad=rcad
print (cad)
# ***************************************
input("...Fin replace...")

# ******************************************************* 
system("clear")
print ("...ljust...")
cad="Python es un lenguaje de programación"
print (cad)
print ("ljust: Ubica una cadena de caracteres a la izquierda en un espacio prefijado")
print ("cad.ljust(espacio,relleno)")
print (cad.ljust(60,"*"))
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





