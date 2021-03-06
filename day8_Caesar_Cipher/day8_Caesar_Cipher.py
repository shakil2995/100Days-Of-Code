import math
import os
import time
from art import logo

#                                         paint calculator
# def calculateCan(height,width,coverage):
#     NoC=(height*width)/coverage
#     return math.ceil(NoC)

# height=int(input("Enter Height of wall : "))
# width=int(input("Width of wall : "))
# cover=int(input("Enter coverage : "))
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
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#                                            encrypt start
def cipher(text, shift, direction):
    shift=shift%27
    en_list = []
    message = ''
    for letter in text:
        if letter not in alphabet:
            en_list.append(letter)
        else:
            letter_index = alphabet.index(letter)
            if direction.lower() == 'encode':
                en_list.append(alphabet[letter_index + shift])
            else:
                en_list.append(alphabet[letter_index - shift])
    for i in en_list:
        message += i
    print(f"The encoded message is {message}\n")


exitFlag = False
os.system('cls')
print(logo)
while not exitFlag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt ,type 'exit' to exit :\n")
    if direction.lower() == 'exit':
        print("Goodbye")
        exitFlag = True
    elif direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        cipher(text, shift, direction)
    else:
        print("invalid input.Please Try Again")