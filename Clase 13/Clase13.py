from os import system
from datetime import date
import platform

def borra():
    so = platform.system()
    if so == "Linux":
        s = "clear"
    else:
        s = "cls"
    system(s)

def profile():
    autor = "Affonso"
    hoy = date.today()
    fecha = [hoy, hoy.day, hoy.month, hoy.year]
    present = "Autor:" + f" {autor}" + f"{fecha}"
    return present

def color():
    f = "\033[0;37"