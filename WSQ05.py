x=int(input("Ingresa la temperatura en Fahrenheit: "))
c=int(5*(x-32)/9)
h=("El agua hierbe a esa temperatura")
nh=("El agua no hierbe a esa temperatura")
C=("La Temperatura en Celsiuos es: "+str(c) )
if c>100:
	print (C + " " + h)
if c<100:
	print (C,nh)