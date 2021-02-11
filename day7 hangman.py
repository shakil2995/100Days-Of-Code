import random
word_list=["tiger","baboon","camel"]
guess=""
#chosen_word=random.choice(word_list)
chosen_word="Tiogoer"
guess=input("Enter a letter : ").lower()
print(guess)
for letters in word_list:
    if letters.lower()==guess.lower():
        print("True")
    else:
        print ("false")