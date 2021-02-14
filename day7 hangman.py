import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
word_list=["tiger","baboon","camel"]
guess=""
display=[]
index=0
chosen_word=random.choice(word_list)
print(chosen_word)
for position in range(len(chosen_word)):
    display.append("_")
end_of_game=False
while not end_of_game:
    guess=input("Guess a letter : ")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter.lower()==guess.lower():
            display[position]=letter
            if "_" not in display:
                end_of_game=True
                print("You Win")
        else:
            print(stages[lives])
            lives=lives-1          
    print(display)
    

