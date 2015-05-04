doc=open("93cars.dat.txt","r") #de modo que abrira ambos archivos
gec=0 #gasolina en la ciudad
geh=0 #gasolina en la carretera
valor=0 #costo
l=1 #contador de líneas leídas
autos=0 #contador de autos
for line in doc: #buscara linea por linea en el documento
    if l%2==1: #cada línea
        gec=gec+float(line[52:54])
        geh=geh+float(line[55:57])
        valor=valor+float(line[42:46])
        autos=autos+1
    l=l+1
pc=round(gec/autos,5) #promedio en ciudad
ph=round(geh/autos,5) #promedio en carretera
pv=round(valor/autos,5)#promedio de costo

#codigo:
print("Existen ",autos," distintos")
print("El promedio de gasolina en la ciudad es: " ,pc)
print("El promedio de gasolina en la carretera es: " ,ph)
print("El promedio del costo de los autos es: " ,pv)
