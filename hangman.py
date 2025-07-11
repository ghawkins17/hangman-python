# Imports the random module, needed for random word selection
import random

# Load words from a text file
def load_words():
    with open('words.txt', 'r') as file:
        return [line.strip() for line in file if line.strip().isalpha()]
all_words = load_words()

# Categorize words by length for different difficulties
short_words = [word for word in all_words if len(word) <= 4]
medium_words = [word for word in all_words if 5 <= len(word) <= 6]
long_words  = [word for word in all_words if len(word) >= 7]

# Welcome the user to the game
print("Welcome to Hangman!")

# Prompts the user to select their difficulty
def choose_difficulty():
    while True:
        difficulty = input("Choose a difficulty (short, medium, long): ").strip().lower()
        if difficulty in ["short", "medium", "long"]:
            break
        print("Invalid difficulty. Please choose 'short', 'medium', or 'long'.")
    if difficulty == "short":
        word = random.choice(short_words)
    elif difficulty == "medium":
        word = random.choice(medium_words)
    else:
        word = random.choice(long_words)
    return word

# Function to ask user to play again
def play_again():
    while True:
        play = input("Do you want to play again? (yes/no): ").strip().lower()
        if play == "yes":
            return True
        elif play == "no":
            print("Thanks for playing! Goodbye!")
            return False
            break
        elif play not in ["yes", "no"]:
            print("Please answer with 'yes' or 'no'.")
            
        

# Main game loop. Calls the difficulty function and manages the game state
def hangman():
    while True:
        word = choose_difficulty()
        masked_word = "_" * len(word)
        guessed_letters = []
        wrong_attempts = 0

        # Tracks the number of wrong attempts and tracks progress towards winning
        while wrong_attempts < 6 and "_" in masked_word:
            print("Guess the word: " + masked_word)
            print(HANGMAN_PICS[wrong_attempts])
            print("Guessed letters: " + ', '.join(guessed_letters))
            guess = input("Enter a letter: ").strip().lower()
            #added for better readability in the console
            print() 
            print()
            # Validation of user letter input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            # Tracks guessed letters
            guessed_letters.append(guess)
            # Checks correctness of the guess
            if guess in word:
                print("Good guess!")
                masked_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
            else:
                wrong_attempts += 1
                print(f"Wrong guess! You have {6 - wrong_attempts} attempts left.")
            
            # Checks if the user lost or won
            if wrong_attempts >= 6 and "_" in masked_word:
                print(HANGMAN_PICS[wrong_attempts]) #prints full hangman at end
                print("Sorry, you've run out of attempts. The word was: " + word)

            if "_" not in masked_word:
                print("Congratulations! You've guessed the word: " + word)
                print(YOU_WIN_ART)

        if not play_again():
            break

# Hangman ASCII art for visual representation of the game state
HANGMAN_PICS = [ '''
     +---+
     |   |
         |
         |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]

#Winner ASCII art
YOU_WIN_ART = r'''
   _           _   _  _  _  _    _            _       
  (_)_       _(_)_(_)(_)(_)(_)_ (_)          (_)      
    (_)_   _(_) (_)          (_)(_)          (_)      
      (_)_(_)   (_)          (_)(_)          (_)      
        (_)     (_)          (_)(_)          (_)      
        (_)     (_)          (_)(_)          (_)      
        (_)     (_)_  _  _  _(_)(_)_  _  _  _(_)      
        (_)       (_)(_)(_)(_)    (_)(_)(_)(_)        
                                                      
                                                      
  _             _  _  _  _  _           _   _         
 (_)           (_)(_)(_)(_)(_) _       (_) (_)        
 (_)           (_)   (_)   (_)(_)_     (_) (_)        
 (_)     _     (_)   (_)   (_)  (_)_   (_) (_)        
 (_)   _(_)_   (_)   (_)   (_)    (_)_ (_) (_)        
 (_)  (_) (_)  (_)   (_)   (_)      (_)(_)            
 (_)_(_)   (_)_(_) _ (_) _ (_)         (_)  _         
   (_)       (_)  (_)(_)(_)(_)         (_) (_)        
   '''
# Starts the program
hangman()