#Pablo Enrique Cárdenas Viera
#A01630814
#Functions
def total(l):
	x=0
	y=0
	while (x<10):
		y=y+(l[x])
		x=x+1
	return y
def average(l):
	x=TO/10
	return x
def standar_deviation(l):
	x=0
	y=0
	z=0
	while (x<10):
		y=((l[x])-AV)**2
		x=x+1
		z=z+y
	import math
	w=math.sqrt(z/AV)
	return w
#Code
l=[]
nums=0
print("List of 10")
while(nums<10):
	n=float(input("Give me a value: "))
	l.append(n)
	nums=nums+1
TO=total(l)
AV=average(l)
DEV=standar_deviation(l)
#Results
print("The total is: "+str(TO))
print("The average is: "+str(AV))
print("The standar deviation is: "+str(DEV))