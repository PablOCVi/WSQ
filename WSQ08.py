#print("Fun with numbers 2 (Pro Version)")
#funcion
def la_suma(x,y):
	respuesta=x+y
	return respuesta
def la_resta(x,y):
	respuesta=x-y
	return respuesta
def la_multiplicacion(x,y):
	respuesta=x*y
	return respuesta
def la_Division_de_enteros(x,y):
	respuesta=x//y
	return respuesta
def el_modulo(x,y):
	respuesta=x%y
	return respuesta
#programa
print("Si ingresas dos numeros el programa desplegara una serie de operaciones.")
x=int(input("Ingresa el primer valor: "))
y=int(input("Ingresa el segundo valor: "))
print("los numeros dados son: "+str(x)+" , "+str(y))
Sum=la_suma(x,y)
print("El resultado de: "+str(x)+" + "+str(y)+" es: "+str(Sum))
Rest=la_resta(x,y)
print("El resultado de: "+str(x)+" - "+str(y)+" es: "+str(Rest))
Multi=la_multiplicacion(x,y)
print("El resultado de: "+str(x)+" * "+str(y)+" es: "+str(Multi))
Divi=la_Division_de_enteros(x,y)
print("El resultado de: "+str(x)+" // "+str(y)+" es: "+str(Divi))
Mod=el_modulo(x,y)
print("El resultado de: "+str(x)+" % "+str(y)+" es: "+str(Mod))