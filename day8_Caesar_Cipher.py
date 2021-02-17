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
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#                                            encrypt start
def cipher(text,shift,direction):
    enList=[]
    Message=''
    if direction.lower()=='encode':
        for letter in text:
            if letter not in alphabet:
                enList.append(letter)
            else:
                LetterIndex=alphabet.index(letter)
                enList.append(alphabet[LetterIndex+shift])
    else:
        for letter in text:
            if letter not in alphabet:
                enList.append(letter)
            else:
                LetterIndex=alphabet.index(letter)
                enList.append(alphabet[LetterIndex-shift])
    for i in enList:
        Message+=i
    print(f"The encoded message is {Message}")
# #                                             encrypt end
# #                                            decrypt start
# def decrypt(text,shift):
#     enList=[]
#     Message=''
#     for letter in text:
#         if letter not in alphabet:
#             enList.append(letter)
#         else:
#             LetterIndex=alphabet.index(letter)
#             enList.append(alphabet[LetterIndex-shift])
#     for i in enList:
#         Message+=i
#     print(f"The decoded message is {Message}")
#                                                decrypt end 

exit=False
os.system('cls')
while exit==False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt ,type 'exit' to exit :\n")
    if direction.lower()=='exit':
        exit=True
    elif direction.lower()!='encode' or direction.lower()!='decode':
        print("Invalid input , please try again.")
        print('\n')
    else :
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        cipher(text,shift,direction)




