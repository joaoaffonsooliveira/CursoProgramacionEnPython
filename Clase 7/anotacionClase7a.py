# Estructura de repeticion while
b = str(input('Ingrese una palabra: ')).strip().upper()
a = 0
while b in('UNO', 'DOS', 'TRES'):
    print('Hola mundo!')
    a += 1
    if a >= 5:
        continue
    else:
        a = 0
        print("Hola!")
print('Salimos')
