from os import system 
from datetime import date
import platform
autor="ROHC"

# Guardamos el sistema operativo del systema
so=platform.system()
if so=="Linux": 
    s="clear"
else: 
    s="cls"
        
# Guardamos la fecha con dia, mes y año
hoy =date.today()
dia =hoy.day
mes =hoy.month
anio=hoy.year

system(s)

print (" Autor: "+f" {autor}".rjust(60,"-"))
print (" Fecha: "+f" {dia}/{mes}/{anio}".rjust(60,"-"))


num=20
while num > 0:
    num -= 1 # num= num-1
    if 10>=num>=5:
        input ("De 10 a 5 no aparece y el ciclo salta al final")
        continue

    print ("La cuenta regresiva vale: ", num)
    
print ("fin del loop")
print ("Valor actual de la variable : ", num)


