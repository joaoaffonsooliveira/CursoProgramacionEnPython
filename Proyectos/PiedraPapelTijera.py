# Juego Piedra Papel Tijera
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

# Unicode Emojis: op[0] es piedra op[1] es papel y op[2] es tijera
op = ["\U0000270A", "\U0001F91A", "\U0000270C"]
e1 = int(input('Vamos jugar Jo Ken Po!\nEscriba uno de los numeros abajo para jugar: \n1 para elegir "\U0000270A" \n2 para elegir "\U0001F91A" \n3 para elegir "\U0000270C"\n'))
if e1 == 1:
    j1 = op[0]
elif e1 == 2:
    j1 = op[1]
elif e1 == 3:
    j1 = op[2]
j2 = random.choice(op)

# Opciones en que el jugador 1 gana
if (j1 == op[0] and j2 == op[2]) or (j1 == op[2] and j2 == op[1]) or (j1 == op[1] and j2 == op[0]):
    print(f'Eligiste: {j1}\n    X \nJugador 2 ha elegido: {j2}  \n{"-"*15}\nGanaste!!')
# Opciones en que los jugadores empatan
elif (j1 == op[0] and j2 == op[0]) or (j1 == op[1] and j2 == op[1]) or (j1 == op[2] and j2 == op[2]):
    print(f'Eligiste: {j1}\n    X \nJugador 2 ha elegido: {j2}  \n{"-"*15}\nLos jugadores han empatado')
# Opciones en que el jugador 1 pierde
else:
    print(f'Eligiste: {j1}\n    X \nJugador 2 ha elegido: {j2}  \n{"-"*15}\nPerdiste!!')