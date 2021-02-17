import math
import os
import time
#                                         paint calculator
# def calculateCan(height,width,coverage):
#     NoC=(height*width)/coverage
#     return math.ceil(NoC)
                                
# height=int(input("Enter Height of wall : "))
# width=int(input("Width of wall : "))
# cover=int(input("Enter coverge : "))
# print(f"You need {calculateCan(height=height,width=width,coverage=cover)} cans of Paint")

#                       Prime number checker

# def CheckIfPrime(number):
#     if number==1:
#         return "Prime"
#     for i in range(2,number):
#         if number%i==0:
#             return "not a Prime"
#     return "a Prime"

# flag=True
# while flag:
#     os.system('cls')
#     number=int(input("Input number to check : "))
#     print(f"{number} is {CheckIfPrime(number)} number")
#     choice=input("\nRun again ? : yes / no : ")
#     if choice.lower()=='yes':
#         flag=True
#     else:
#         print("Program will now exit.")
#         time.sleep(1)
#         flag=False

#                          Caesar Cipher



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text,shift):
    enList=[]
    Message=''
    for letter in text:
        LetterIndex=alphabet.index(letter)
        if LetterIndex>=26-shift:
            LetterIndex=-shift
        enList.append(alphabet[LetterIndex+shift])
    for i in enList:
        Message+=i
    print(Message)

def decrypt(text,shift):
    enList=[]
    Message=''
    for letter in text:
        LetterIndex=alphabet.index(letter)
        print(alphabet[LetterIndex])
        if LetterIndex+shift<0:
            LetterIndex+=shift
        enList.append(alphabet[LetterIndex-shift])
    for i in enList:
        Message+=i
    print(Message)
exit=False
while exit==False:
    os.system('cls')
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt ,type 'exit' to exit :\n")
    if direction.lower=='exit':
        exit=True
    elif direction.lower()=='encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text,shift)
    elif direction.lower()=='decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text,shift)
    else:
        print("Invalid input , please try again.")


