# Juego Piedra Papel Tijera

import random
# Unicode Emojis: op[0] es piedra op[1] es papel y op[2] es tijera
op = ["\U0000270A", "\U0001F91A", "\U0000270C"]
j1 = random.choice(op)
j2 = random.choice(op)

if (j1 == op[0] and j2 == op[2]) or (j1 == op[2] and j2 == op[1]) or (j1 == op[1] and j2 == op[0]):
    print(f'Jugador 1: {j1}\n    X \nJugador 2: {j2}  \n{"-"*15}\nJugador 1 ha ganado!!')
elif (j1 == op[0] and j2 == op[0]) or (j1 == op[1] and j2 == op[1]) or (j1 == op[2] and j2 == op[2]):
    print(f'Jugador 1: {j1}\n    X \nJugador 2: {j2}  \n{"-"*15}\nLos jugadores han empatado')
else:
    print(f'Jugador 1: {j1}\n    X \nJugador 2: {j2}  \n{"-"*15}\nJugador 1 ha perdido!!')

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