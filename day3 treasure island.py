#                                            tiket calculator
# payment=0
# height=0
# height=int(float(input("Enter height in cm : ")))
# if height>=120:
#     age=int(input("Enter your age : "))
#     if age<=12:
#         print("Pay 5$")
#         payment=5
#     elif age<=18:
#         print("print 7$")
#         payment=7
#     else:
#         print("Pay 12$")
#         payment=12
#     inPhotos=input("Do you want photos ? yes/no : ")
#     if inPhotos=='yes':
#         print(f"Total bill is {payment+3}")
#     else:
#         print(f"Total bill is {payment}")
# else:
#     print("You Can't Ride.")

#                                       Tresture Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Treasu]
*******************************************************************************
''')
print("Welcome to Tresture Island")
print("Your mission is to find the Tresture")
decission=(input("You're at a crossroad. Where do you want to go ? Left or Right ? : "))
if decission=='right'or decission=='Right':
    print("You are lost , Game over.")
elif decission=='left'or  decission=='Left':
    decission=input('You come to a lake. There is an island in the middle of the lake\nType "wait" to wait for a boat.Type "Swim" to swim across : ')
    if decission=='swim'or decission=='Swim':
        print("You were eaten by a shark, Game over.")
    elif decission=='wait'or  decission=='Wait':
        decission=input('You arrive at the island unharmed. There is a house with three doors. One red , One yellow and one blue\nWhich color do you choose ? : ')
        if decission=='red'or'Red':
            print("Fire came out of the room and you died.Game over.")
        elif decission=='blue'or decission=='Blue':
            print("Water came out off the room and you got flooded.Game over.")
        else :
            print("You have found the treasure box. Wou win.")
else:
    print("you failed to make a decission, Game over.")
