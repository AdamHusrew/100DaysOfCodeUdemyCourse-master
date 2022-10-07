import random

logo = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   '''

print(logo)
print("Welcome to HangMan game!!!")

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
                     'coyote crow deer dog donkey duck eagle ferret fox frog goat '
                     'goose hawk lion lizard llama mole monkey moose mouse mule newt '
                     'otter owl panda parrot pigeon python rabbit ram rat raven '
                     'rhino salmon seal shark sheep skunk sloth snake spider '
                     'stork swan tiger toad trout turkey turtle weasel whale wolf '
                     'wombat zebra ').split()

chosen_word = word_list[round((random.random()) * 5)]

# chosen_word = random.choice(word_list)
display = []

for _ in chosen_word:
    display.append("-")

print(display)
# mistakes = 3 + int(len(chosen_word) * 0.25)
mistakes = 6

for i in range(len(chosen_word) * 3):
    guess = input("Guess a letter: ").lower()
    hasWord = False
    for j in range(len(chosen_word)):
        if chosen_word[j] == guess:
            display[j] = guess
            hasWord = True

    if hasWord:
        print(f"You have guessed letter {guess}")
        print(display)
    else:
        mistakes -= 1
        if mistakes == 0:
            print("You have used your all chances. Game over!!!")
            print(stages[6 - mistakes])
            exit()
        else:
            print(f"No Match...Try again...And you have {mistakes} chance to guess")
            print(stages[6 - mistakes])
