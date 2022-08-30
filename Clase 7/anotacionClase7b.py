from os import system
while True:
    print("1 piedra")
    print("2 tijera")
    print("3 papel")
    print("S salir")
    op = input('Selecioná opción: ')
    if op == "1":
        system("piedra.py")
    if op == "2":
        system("tijera.py")
    if op == "3":
        system("papel.py")
    elif op.upper() == "S":
        exit()