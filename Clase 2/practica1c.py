from os import system
from datetime import date

hoy=date.today()
autor='Joao Affonso'
print('Autor: ', autor)
print('Fecha: ', hoy)
tpv = input("Ingrese tipo de vehículo: ")
mar = input("Ingrese la marca del vehículo: ")
mod = input("Ingrese modelo del vehículo: ")
ano = input("Ingrese año del vehículo: ")
col = input("Ingrese el color del vehículo: ")

print(f""" El tipo del vehículo es {tpv}, marca {mar}, modelo {mod}, año {ano}, color {col}""")