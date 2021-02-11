import random
word_list=["tiger","baboon","camel"]
guess=""
display=[]
index=0
#chosen_word=random.choice(word_list)
chosen_word="baboon"
guess=input("Enter a letter : ").lower()
for letter in chosen_word:
    display.append("_")
print (chosen_word)
for i in range(0,100):
    if "_" not in display:
        break
    for letter in chosen_word:
        if letter.lower()==guess.lower():
            display[index]=f"{guess}"
    index=index+1   
    print(display)
