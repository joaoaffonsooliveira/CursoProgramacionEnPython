from os import system
from datetime import date


autor = "ROHC"
tema  = "Cadena de carateres"
hoy   = date.today()
system("cls")
print (autor,"                             ", hoy)
print ("Funciones de cadena")
cadena=input ("Ingresar una oración: ")
print ("capitalize: Escribe en mayúscula la 1er letra de una cadena")
print (cadena.capitalize())
input ("...Fin capitalize...")

system("cls")
print (autor,"                             ", hoy)
print ("Funciones de cadena")
cadena=input ("Ingresar una oración: ")
print ("lower: Escribe en minúsculas toda la cadena")
print (cadena.lower())
input ("...Fin lower...")

system("cls")
print (autor,"                             ", hoy)
print ("Funciones de cadena")
cadena=input ("Ingresar una oración: ")
print ("upper: Escribe en mayúsculas toda la cadena")
print (cadena.upper())
input ("...Fin upper...")

system("cls")
print (autor,"                             ", hoy)
print ("Funciones de cadena")
cadena=input ("Ingresar una oración: ")
print ("title: Escribe en mayúscula cada palabra de toda la cadena")
print (cadena.title())
input ("...Fin title...")


system("cls")
print ("Funciones de cadena")
print ("casefold:   Método agresivo para convertir a minusculas una cadena")
print ("encode:     Método para dar un tipo de codificación a una cadena")
print ("endswith:   Devuelve True si una cadena termina con el sufijo especificado. Si no, vuelve False.")
print ("expandtabs: Distribuye un acadena con tabulaciones con valores fijados")
