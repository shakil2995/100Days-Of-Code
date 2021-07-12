import os

ErrorRate = 0
def func(x):
    return x*x*x - 4*x -9

def bisection(a,b):
    if (func(a) * func(b) >= 0):
            print("Root not found for a and b\n")
            return
    counts=0
    c = a
    while ((b-a) >= ErrorRate):
        counts=counts+1

        c = (a+b)/2
 
        if (func(c) == 0.0):
            break


        elif (func(c)*func(a) < 0):
            b = c
        else:
            a = c
            print("Number of iteration=",counts)
            print("The value of root is : ",c)
        print("")
        print("Total Number of iteration=",counts)
        print("The value of root is : ",c)

a=b=0
print("Solving function : x3-4x-9 using Bisection Method \n" )
a=float(input("Initial value for lower limit="))
b=float(input("Initial value for upper limit="))
ErrorRate=float(input("Give error rate : "))
bisection(a, b)
os.system("pause")
#x3-4x-9