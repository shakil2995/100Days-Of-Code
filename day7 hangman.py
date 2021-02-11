import random
word_list=["tiger","baboon","camel"]
guess=""
display=[]
index=0
#chosen_word=random.choice(word_list)
chosen_word="baboon"
for letter in chosen_word:
    display.append("_")
print (chosen_word)
print(display)
guess=input("Enter a letter : ")
while "_" not in display:
    for letter in chosen_word:
        if letter.lower()==guess.lower():
            display[index]=f"{guess}"
        index=index+1   
    print(display)
