# Juego Piedra Papel Tijera
import random
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

if (j1 == op[0] and j2 == op[2]) or (j1 == op[2] and j2 == op[1]) or (j1 == op[1] and j2 == op[0]):
    print(f'Eligiste: {j1}\n    X \nJugador 2 ha elegido: {j2}  \n{"-"*15}\nGanaste!!')
elif (j1 == op[0] and j2 == op[0]) or (j1 == op[1] and j2 == op[1]) or (j1 == op[2] and j2 == op[2]):
    print(f'Eligiste: {j1}\n    X \nJugador 2 ha elegido: {j2}  \n{"-"*15}\nLos jugadores han empatado')
else:
    print(f'Eligiste: {j1}\n    X \nJugador 2 ha elegido: {j2}  \n{"-"*15}\nPerdiste!!')

# Abajo hay una variación del ejercicio anterior usando el modulo emoji
"""
import random
import emoji
op = [emoji.emojize(':puño_en_alto:', language='es').strip(), emoji.emojize(':mano_abierta:', language='es'), emoji.emojize(':mano_con_señal_de_victoria:', language='es')]
j1 = random.choice(op)
j2 = random.choice(op)

if (j1 == op[0] and j2 == op[2]) or (j1 == op[2] and j2 == op[1]) or (j1 == op[1] and j2 == op[0]):
    print(f'Jugador 1: {j1}\n    X \nJugador 2: {j2}  \n{"-"*15}\nJugador 1 ha ganado!!')
elif (j1 == op[0] and j2 == op[0]) or (j1 == op[1] and j2 == op[1]) or (j1 == op[2] and j2 == op[2]):
    print(f'Jugador 1: {j1}\n    X \nJugador 2: {j2}  \n{"-"*15}\nLos jugadores han empatado')
else:
    print(f'Jugador 1: {j1}\n    X \nJugador 2: {j2}  \n{"-"*15}\nJugador 1 ha perdido!!')
"""