#Pablo Enrique Cárdenas Viera
#A01630814
    #Function


def Greatest_Common_Divisor(x,y):
    if ((x%y)!=0):
        return "1"
    if(x>y):
        while(x>y):
            x=x-y
            res=x
    elif(x==y):
        res=x
    else:
        while(x<y):
            y==y-x
            res=y
    return res
    
    
x=int(input("Type the first value: "))
y=int(input("Type the second value: "))
Result=Greatest_Common_Divisor(x,y)
    #Result
print ("The greatest common divisor is: "+str(Result))


