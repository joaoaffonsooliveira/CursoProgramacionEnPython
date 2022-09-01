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
while num>0:
    print (num)
    num -= 1 # num= num-1
    if num==5:
        pass
    
print ("fin del loop")
print ("Valor actual de la variable : ", num)


