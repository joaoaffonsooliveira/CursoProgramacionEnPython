from os import system
from datetime import date

system("cls")
hoy=date.today()
autor="Joao Affonso"
print('Autor: ', autor)
print('Fecha: ', hoy)
esp = input("Ingrese especie: ")
raz = input("   Ingrese raza: ")
col = input("  Ingrese color: ")
eda = input("   Ingrese edad: ")

print(f""" La especie es {esp}, la raza es {raz}, el color es {col}, y la edad es {eda}""")
