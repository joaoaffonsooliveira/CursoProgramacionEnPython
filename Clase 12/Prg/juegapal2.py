from random import choice
from os import system
larc=["python","proceso","programa","computadora"]
lc=choice(larc)
lpal=[]	
l=len(lc)
for j in range(l):
	lpal.append("_")

def donde(pal, let):
	pos =[]	
	l=len(pal)
	for i in range(l):
		if let ==pal[i]:
			pos.append(i)
	print (pos)
	input(" ")		
	return pos		


	

while l>0:
	system("clear")
	print (f"\t{lc}")
	print ("\n\t",end="")

	for i in range(l):
		print (lpal[i], end="")
	print ("\n"*2)
	

	letra=input("ingresar letra a buscar: ")
	p= donde(lc,letra)
	print("Posiciones: ",p)
	
	if p!=[]:
		for cl in p:
			for j in range (len(lc)):
				if letra==lc[j]:
					lpal[j]=letra
	else:
		print ("No esta esa letra")
		
		input(" ")
