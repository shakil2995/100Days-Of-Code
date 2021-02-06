#                     LIST SPLIT and RANDOM
# import random
# print(f"{random.choice(input('Input all the names with a , : ').split(', '))} will give the bill")

#                     Treasure hunt
while True:
    print(" ")
    row1=["🥵","🥵","🥵"]
    row2=["🥵","🥵","🥵"]
    row3=["🥵","🥵","🥵"]
    map=[row1,row2,row3]
    print(f"{row1}\n{row2}\n{row3}")
    treasureloc=input('where do you want to put the treasure ? : ')
    loc1=int(treasureloc[0])
    loc2=int(treasureloc[1])
    if loc1-1>2 or loc2-1>2:
        print("Invalid location")
        print("Please try again")
    else:    
        map[loc1-1][loc2-1]="😀"
        print(f"{row1}\n{row2}\n{row3}")