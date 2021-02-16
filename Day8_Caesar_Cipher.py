import math
def calculateCan(height,width,coverage):
    NoC=(height*width)/coverage
    return math.ceil(NoC)
                                
height=int(input("Enter Height of wall : "))
width=int(input("Width of wall : "))
cover=int(input("Enter coverge : "))
print(f"You need {calculateCan(height=height,width=width,coverage=cover)} cans of Paint")







