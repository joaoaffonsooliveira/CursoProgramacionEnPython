#!/usr/bin/python3.8
from os import system 
from datetime import date
from random import choice
import platform
autor="ROHC"

# Guardamos el sistema operativo del systema
so=platform.system()
if so=="Linux":
  s="clear"
else:
  s="cls"
    
# Guardamos la fecha con dia, mes y año
hoy =date.today()
dia =hoy.day
mes =hoy.month
anio=hoy.year
system(s)
print (f" Autor: {autor}"+f" {dia}/{mes}/{anio}".rjust(40," "))
print(" 1ra forma ".center(30,"*"))
ing= input("Desea hacer un ingreso: ")
while ing.upper() == "S":
    nom= input("        Ingrese nombre: ")
    ape= input("      Ingrese apellido: ")
    print(f"Ingreso: {nom} {ape}")
    ing= input("Desea hacer un ingreso: ")
    


system(s)
print (f" Autor: {autor}"+f" {dia}/{mes}/{anio}".rjust(40," "))
print(" 2da forma ".center(30,"*"))

#input en Python
while (input("Desea hacer un ingreso: ")).upper() == "S":
    nom=input("        Ingrese nombre: ")
    ape=input("      Ingrese apellido: ")
    print(f"Ingreso: {nom} {ape}")
   

