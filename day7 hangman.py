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
  print(stages[lives])
  guess=input("Guess a letter : ")
  flag=False
  flag2=True
  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if guess.lower() in display and flag2==True:
      print("You have already guessed this letter . Try again. ")
      flag=True
      flag2=False
    elif letter.lower()==guess.lower():
      display[position]=letter
      flag=True
      flag2=False
      if "_" not in display:
          end_of_game=True
          print("\nYou have guessed the correct word.\n   ######### You Win #########")
    elif flag==False and position==len(chosen_word)-1:
      lives=lives-1
      if (lives==0):
        end_of_game=True
        print("\nYou ran out of life .You lose")
      else:
        print(f"\nYou guessed {guess},that is not in the word. You lose a life .")
      
  print("\n")    
  print(display)

  #print(stages[lives])

    

