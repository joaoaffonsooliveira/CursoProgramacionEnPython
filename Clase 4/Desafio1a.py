from os import system
from datetime import date
import platform
autor ='Joao Affonso'
hoy=date.today()
so=platform.system()

if so == 'linux':
	s= 'clear'
else:
	s= 'cls'
system(s)

print(autor)
print(hoy)

'''Ingresando numeros'''

a= int(input('ingrese un numero: '))
b= int(input('ingrese el segundo numero: '))
c= int(input('ingrese el tercer numero: '))

'''comparación entre a, b y c'''

if a == b and a == c:
	print(f"{a}, {b} y {c} son iguales")
elif a == :
	print(f"{a} es igual a {b}")
elif b == c:
	print(f"{b} es igual a {c}")
elif a > b:
	print(f"{a} es mayor que {b}")
elif a > c:
	print(f"{a} es mayor que {c}")
elif b > a:
	print(f"{b} es mayor que {a}")
elif b > c:
	print(f"{b} es mayor que {c}")
elif c > a:
	print(f"{c} es mayor que {a}")
else:
	print(f"{c} es mayor que {b}")
