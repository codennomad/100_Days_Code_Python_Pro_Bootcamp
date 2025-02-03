import random

#World list
word_list = ["aardvark", "baboon", "camel"]

#Initial number of lives
lives = 6

#hangman logo
print('''
      
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  
                                    aa,    ,88                                
                                     "Y8bbdP"    ''')
print("Welcome to Hangman ! Guess the word before you run out of lives")

#Hangman stages (graphical representation)
stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
    ]

#Randomly select a word
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

#Create the placeholter for the letters (hidden word)
display = ["_"] * word_lenght

#set to track guessed letter
guessed_letters = set()

#Game stage
game_over = False

#Main game loop
while not game_over:
    print(f"\n{' '.join(display)}")
    print(f"Lives Remaining: {lives}")
    print(stages[lives])
    
    #Prompt the player for a letter
    guess = input("Guess a letter: ").lower()
    
    #check if the letter has already been guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again!")
        continue

    #Add letter to the set of guessed letters
    guessed_letters.add(guess)
    
    #check if the guessed letter is in the world
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
        print(f"Good job! '{guess}' is in the word.")
    else:
        #Reduce the number of lives if the letter is not in the word
        lives -= 1
        print(f"Wrong guess! '{guess}' is not in the word.")
        if lives == 0:
            game_over = True
            print("\n*********************** YOU LOSE *************************")
            print(f"The word was: {chosen_word}")
          
    #check if the player has guessed all the letters        
    if "_" not in display:
        game_over = True
        print("\n************************ YOU WIN *************************")
        print(f"THE WORD WAS: {chosen_word}")
        print("************************************************************")
        
        
