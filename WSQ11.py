#Pablo Enrique Cárdenas Viera
#A01630814
#Function
def inverse(P):
    P =str(P)
    P = P[::-1]
    P =int(P)
    return P
#Code
print ("This program going to print 3 aspects about the range of number you input")
num=[]
lyc=[]
A = int(input("From wich value: "))
U = int(input("To wich value: "))
print ("The range of numbers checked is: %s to %s" %(A,U))
for i in range(U-A+1):
    num.append(A)
    A = A+1
L=0
I=0
N=0
for i in num:
    A = inverse(i)
    if i== A:
        L = L+1
    else:
        E = i + A
        A = inverse(E)
        for q in range(30):
            if E == A:
                I = I+1
                break
            else:
                E = E + A
                A = inverse(E)
                if q == 29:
                    N = l+1
                    lyc.append(i)
print ('The number of natural palindromes is : %s' %(L))
print ('The number of Non-Lychrel numbers is: %s' %(I))
print ('The number of Lychrel number candidates is: %s' %(N))
if N!= 0:
    print ("The Lychrel number candidates is:")
    print (lyc)