import random
import os
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    
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
word_list=["tiger","baboon","camel","horse","elephant","monkey"]
guess=""
display=[]
index=0
chosen_word=random.choice(word_list)
print(chosen_word)
for position in range(len(chosen_word)):
    display.append("_")
end_of_game=False
os.system('cls')
print(logo)
while not end_of_game:
  guess=input("Guess a letter : ")
  os.system('cls')
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
          print("You have guessed the correct word.\n   ######### You Win #########")
    elif flag==False and position==len(chosen_word)-1:
      lives=lives-1
      if (lives<=3):
        print("Hint : "+chosen_word[lives])

      if (lives==0):
        end_of_game=True
        print("You ran out of life .You lose")
      else:
        print(f"You guessed {guess},that is not in the word. You lose a life .")
      
  print(display)
  print(stages[lives])
  #print(stages[lives])

    

