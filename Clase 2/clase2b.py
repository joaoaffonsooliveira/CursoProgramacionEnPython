from os import system
from datetime import date
system("cls")
hoy=date.today()
autor= "Ruben"
nom = input("      Ingrese nombre: ")
ape = input("    Ingrese apellido: ")
bar = input("        Ingrese edad: ")
eda = input("      Ingrese barrio: ")
nac = input("Ingrese nacionalidad: ")
print("El nombre es: ", nom)
print("El apellido es: ",ape)
print("La edad es: ", eda)
print("El barrio es: ", bar)
print("La nacionalidad es: ", nac)
