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
    enMessage=''
    for letter in text:
        LetterIndex=alphabet.index(letter)
        if LetterIndex>=20:
            LetterIndex=0
        enList.append(alphabet[LetterIndex+shift])
    for i in enList:
        enMessage+=i
    print(enMessage)

def decrypt(text,shift):
    enList=[]
    enMessage=''
    for letter in text:
        LetterIndex=alphabet.index(letter)
        print(LetterIndex)
        if LetterIndex<=5:
            LetterIndex=26
        enList.append(alphabet[LetterIndex-shift])
    for i in enList:
        enMessage+=i
    print(enMessage)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt(text,shift)
encrypt("civilization",5)
decrypt('hnfnqnffynts',5)

