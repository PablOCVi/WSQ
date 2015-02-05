from random import randint
x=(randint (1,100))
z=0
print ("Tengo un numero del 1 al 100")
print("Trata de adivinarlo...")

y=int(input("AHORA: "))
while (y!=x):
	z=(z+1)
	if y>x:
		print("lo siento, pero:",str(y),"es muy alto")
	if y<x:
		print("Lo siento, pero:",str(y),"es muy bajo")
	print("Intentalo Nuevamente")
	y=int(input("AHORA: "))
print(str(y),"es el numero!!!, Genial")
print("Tan solo fallaste:",str(z),"veces")