from os import system
from datetime import date
system("cls")
hoy=date.today()
autor= "João Affonso"
print('Autor: ', autor)
print('Fecha: ', hoy)
nom = input("      Ingrese nombre: ")
ape = input("    Ingrese apellido: ")
eda = input("        Ingrese edad: ")
dir = input("      Ingrese dirección: ")
tel = input("Ingrese numero de telefono: ")

print(f""" El nombre es {nom}, El apellido es {ape}, La edad es {eda}, la direccion es {dir}, el telefono es {tel}""")