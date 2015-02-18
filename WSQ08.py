#print("Fun with numbers 2 (Pro Version)")
x=int(input("Ingresa el primer valor: "))
y=int(input("Ingresa el segundo valor: "))
operaciones=[]
operaciones.append("La suma es: "+str(x+y))
operaciones.append("La resta es: "+str(x-y))
operaciones.append("La division en enteros es: "+str(x//y))
operaciones.append("La division en floats es: "+str(x/y))
operaciones.append("La multiplicacion es: "+str(x*y))
operaciones.append("El modulo es: "+str(x%y))
for i in range(-1,-6,-1):
	print(operaciones[i])	
