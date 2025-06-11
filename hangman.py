import random

# List of possible words to guess
# ye 5 word hai jo mujhe guess krne hai agr maine glt kiya to fanshi
word_list = ['farcry','chess','rockstar','asphalt','pubg','payback']

def choose_word():
    """Select a random word from the word list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Display the word with underscores for unguessed letters."""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman_graphics(tries):
    """Return the hangman graphics based on the number of wrong tries."""
    hangman_graphics = [
        """
           ------
           |    |
                |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        ---------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        ---------
        """
    ]
    return hangman_graphics[tries]

def play_game():
    print("Welcome to Hangman!")
    
    word = choose_word()
    guessed_letters = []
    tries = 0
    max_tries = 6
    
    while tries < max_tries:
        print(hangman_graphics(tries))
        print("Word: ", display_word(word, guessed_letters))
        print("Guessed letters: ", ', '.join(guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            tries += 1
        
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print(hangman_graphics(tries))
        print("Game over! The word was:", word)

if __name__ == "__main__":
    play_game()