#                                            tiket calculator
payment=0
height=int(input("Enter height in cm : "))
if height>=120:
    age=int(input("Enter your age : "))
    if age<=12:
        print("Pay 5$")
        payment=5
    elif age<=18:
        print("print 7$")
        payment=7
    else:
        print("Pay 12$")
        payment=12
    inPhotos=input("Do you want photos ? yes/no : ")
    if inPhotos=='yes':
        print(f"Total bill is {payment+3}")
    else:
        print(f"Total bill is {payment}")
else:
    print("You Can't Ride.")