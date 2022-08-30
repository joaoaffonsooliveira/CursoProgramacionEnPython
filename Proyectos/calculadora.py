# Calculadora en Python
from os import system
from datetime import date
import random
import platform
autor = "Joao Affonso"

so = platform.system()
if so == "Linux":
    s = "clear"
else:
    s = "cls"

hoy = date.today()
dia = hoy.day
mes = hoy.month
anio = hoy.year

system(s)

print("Autor: "+f" {autor}".rjust(100, "-"))
print("Fecha: "+f" {dia}/{mes}/{anio}".rjust(100, "-"))

n1 = float(input('Escriba el primer número: '))
op = str(input('Qué operación matemática desea realizar? '))
n2 = float(input('Escriba el segundo número: '))
if op == '+':
    print(f'{n1} + {n2} = {n1 + n2}')
elif op == '-':
    print(f'{n1} - {n2} = {n1 - n2}')
elif op == '*':
    print(f'{n1} x {n2} = {n1 * n2}')
elif op == '/':
    print(f'{n1} / {n2} = {n1 / n2}')
elif op == '^':
    print(f'{n1} ^ {n2} = {n1**n2}')