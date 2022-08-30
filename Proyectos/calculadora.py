# Calculadora en Python
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