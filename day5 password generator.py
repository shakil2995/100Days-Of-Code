#      largest number
# numberlist=input("Input numbers : ").split()
# for n in range(0,len(numberlist)):
#     numberlist[n]=int(numberlist[n])
# print(numberlist)
# largest=0
# for number in numberlist:
#     if largest<number:
#         largest = number
# print(f"Largest number = {largest}")

#               fizz buzz
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print ("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

#                        password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_text=""
pass_length=nr_letters+nr_symbols+nr_numbers

while pass_length!=0:
    rand=random.randint(0,2)
    if pass_length==0:
        break
    elif rand==0 and nr_letters!=0:
        password_text+=(random.choice(letters))
        nr_letters-=1
        pass_length-=1
    elif rand==2 and nr_symbols!=0:
        password_text+=(random.choice(symbols))
        nr_symbols-=1
        pass_length-=1
    elif rand==1 and nr_numbers!=0:
        password_text+=(random.choice(numbers))
        nr_numbers-=1
        pass_length-=1

print(f"Your generated password is : {password_text}")

#random.shuffle(listName)