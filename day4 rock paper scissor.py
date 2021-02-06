#                     LIST SPLIT and RANDOM
#import random
# print(f"{random.choice(input('Input all the names with a , : ').split(', '))} will give the bill")

#                     Treasure hunt
# while True:
#     print(" ")
#     row1=["🥵","🥵","🥵"]
#     row2=["🥵","🥵","🥵"]
#     row3=["🥵","🥵","🥵"]
#     map=[row1,row2,row3]
#     print(f"{row1}\n{row2}\n{row3}")
#     treasureloc=input('where do you want to put the treasure ? : ')
#     loc1=int(treasureloc[0])
#     loc2=int(treasureloc[1])
#     if loc1-1>2 or loc2-1>2:
#         print("Invalid location")
#         print("Please try again")
#     else:    
#         map[loc1-1][loc2-1]="😀"
#         print(f"{row1}\n{row2}\n{row3}")

#                    Rock Paper Scissors

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
x=True
while x==True:
        userInput=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.3 to exit : "))
        if userInput==3:
            x=False
            print("Game will now exit. ")
        elif userInput>3:
            print("Invalid input . try again ")
        else:
            print("\nyou chose :")
            imagesText=['Rock','Paper','Scissors']
            images=[rock,paper,scissors]
            print(images[userInput])
            computerChoice=random.randint(0,2)
            print("Computer chose : ")
            print(images[computerChoice])
            if userInput==computerChoice:
                print("Both chose same . It's a draw. ")
            elif userInput==0 and computerChoice == 1:
                print(f"{imagesText[computerChoice]} beats {imagesText[userInput]}. you loose")
            elif userInput==1 and computerChoice == 2:
                print(f"{imagesText[computerChoice]} beats {imagesText[userInput]}. you loose")
            elif userInput==2 and computerChoice == 0:
                print(f"{imagesText[computerChoice]} beats {imagesText[userInput]}. you loose")
            else:
                print(f"{imagesText[userInput]} beats {imagesText[computerChoice]}. you win")