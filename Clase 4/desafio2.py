from os import system
from datetime import date
import platform

autor = 'Joao Affonso'
hoy = date.today()
so = platform.system()

if so == 'linux':
	s= "clear"
else:
	s= "cls"
system()

print(autor)
print(hoy)

pal1= input('Ingrese la palabra uno: ')
pal2= input('Ingrese la palabra dos: ')
num1= int(input('Ingrese el primer numero: '))
num2= int(input('Ingrese el segundo numero: '))

if pal1 == pal2:
	print(f'La palabra {pal1} es igual a la palabra {pal2}')
else:
	print(f'La palabra {pal1} es distinta de la palabra {pal2}')

if num1 == num2:
	print(f'El numero {num1} es igual al {num2}')
else:
	print(f'El numero {num1} es distinto del numero {num2}')


