from os import system
lista = ['Perú', 'Equador', 'Chile']
paises = ['Argentina', 'Brasil', 'Venezuela', 'Uruguay', 'Cuba']

# Usamos el método sort para ordenar alfabeticamente
a = paises
a.sort()
print(paises)
input('...')
print(a)
input('...')
b = paises
b.reverse()
print(paises)
input('...')
print(b)
input('...')
paises.sort()
print(paises)
input('...')

# Usamos el método reverse para que tengamos la inversa
paises.reverse()
print(paises)
input('...')

# Usamos el método append para agregar un elemento al final de la lista
paises.append(lista)
m = len(paises)
for i in range(m):
    print(i, paises[i])
input('...')

# Usamos el método extend para agregar una lista a otra lista
paises.extend(lista)
n = len(paises)
for i in range(n):
    print(i, paises[i])
input('...')