from os import system 
from datetime import date
import platform
import random

def borra():
    so=platform.system()
    if so=="Linux": 
        s="clear"
    else: 
        s="cls"
    system(s)   
        
def profile():
    autor="ROHC"
    hoy=date.today()
    fecha =[hoy,hoy.day,hoy.month,hoy.year]
    print (" Autor: "+f" {autor}"+f" {fecha[1]}/{fecha[2]}/{fecha[3]}".rjust(60,"-"))
"""
Las funciones random son funciones 
psedudo aleatorias que tiene un sin número
de aplicaciones en variados campos
"""
"""
Utilizadas en matemáticas, estadisticas, juegos,
simuladores, ciencias sociales, modelado, simulaciones
analisis de datos, pruebas, testeos, etc
"""
# randint() 
# Devuelve un valor entero entre 2 enteros
# Los valores extremos estan incluidos
input("********** randint() **********")
print("Entre 5 y 25")
print(random.randint(5,25))

# randrange()
# Esta funcion es similar a la funcion anterior
# Agrega al rango un paso determinado
# La siguiente funcion devuelve un valor 
# entre 6 y 51, multiplo de 6
# Si no se define el paso será 1

input("********** randrange() **********")
print("Entre 6 y 51 seleccionado de a 6")
print (random.randrange(6, 51, 6))

input("********** random() **********")
# random() devuelve un flotante entre 0 y 1
print("Entre 0 y 1")
print (random.random())

# uniform() devuelve un valor flotante 
# entre dos valores cualesquiera
input("********** uniform() **********")
print("Entre 50 y 80")
print (random.uniform(50,80))

# seed()  
"""
Cuando te interese obtener varias veces 
la misma secuencia de números pseudoaleatoria 
se puede utilizar la función seed() que fija 
mediante una "semilla" el mismo comienzo en 
cada secuencia, permitiendo con ello obtener 
series con los mismos valores. 
"""
input("********** seed() **********")
regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
           'patín', 'balón', 'reloj', 'bicicleta', 'anillo']

for serie in range(3):
    print('\nserie:', serie + 1)
    random.seed(0)
    for sorteo in range(5):
        regalo = regalos[random.randint(0, 9)]
        print('Sorteo', sorteo + 1, ':', regalo)

# choice selecciona de una lista de elementos
input("********** choice() **********")
print (random.choice(["gato","perro","león","mono","cocodrilo"]))

# shuffle() mezcla los elementos de de una lista
input("********** shuffle() **********")
lista=["As","Jack","Dame","Roi"]
print ("Mezcla: ",lista)
for i in range (5):
    random.shuffle(lista)
    print (lista)

# sample() selecciona una lista al azar de una lista dada
# Seleccionamos 5 listas de 3 elementos
input("********** sample() **********")
lista=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
print( "Selecciona 3 elementos de: ",lista)
for i in range(5):
    print (random.sample(lista,3))

