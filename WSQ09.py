#funcion
def factorial(x):
	a=x
	respuesta=1
	while (a>1):
		respuesta=respuesta*a
		a=a-1
	return respuesta
#code
print("Si ingresas un numero positivo, desplegare el factorial del mismo.")
y=1
x=int(input("Ingresa un numero positivo: "))
Fac=factorial(x)
if (x>0):
	print("El factorial de: "+str(x)+" es: "+str(Fac))