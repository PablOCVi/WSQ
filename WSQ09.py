#function
def factorial(x):
	a=x
	respuesta=1
	while (a>1):
		respuesta=respuesta*a
		a=a-1
	return respuesta
#code
print("Si ingresas un numero positivo, desplegare el factorial del mismo.")
n="n"
z=""
while (z!=n):
	x=int(input("Ingresa un numero positivo: "))
	Fac=factorial(x)
	if (x>0 or x==0):
		print("El factorial de: "+str(x)+" es: "+str(Fac))
		z=str(input("Necesitas el factorial de otro numero, presiona cualqioer tecla, si no,ingresa n.): "))
print("Adios!")
	