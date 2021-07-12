
# function x^2+x-1;
ErrorRate = .001
def func(x):
    return x*x + x -1

#  Prints root of func(x) with ErrorRate
def bisection(a,b):
    if (func(a) * func(b) >= 0):
            print("You have not assumed right a and b\n")
            return
    counts=0
    c = a
    while ((b-a) >= ErrorRate):
        counts=counts+1
            # Find middle point
        c = (a+b)/2
        # Check if middle point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        elif (func(c)*func(a) < 0):
            b = c
        else:
            a = c
            print("Number of iteration=",counts)
            print("The value of root is : ",c)
        print("")
        print("Total Number of iteration=",counts)
        print("The value of root is : ",c)

# Driver program to test above function
    # Initial values assumed
a=b=0
print("x^2+x-1")
a=int(input("initial value for lower limit="))
b=int(input("initial value for upper limit="))
bisection(a, b)