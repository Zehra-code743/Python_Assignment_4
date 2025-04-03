import random  # Import the random module to choose a word randomly

def choose_word():
    """Function to choose a random word from a predefined list"""
    words = ['python', 'developer', 'hangman', 'programming', 'computer']  # List of words
    return random.choice(words)  # Return a random word from the list

def display_word(word, guessed_letters):
    """Function to display the word with guessed letters revealed"""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)  # Show guessed letters

def hangman():
    """Main function to play the Hangman game"""
    word = choose_word()  # Select a random word
    guessed_letters = set()  # Set to store guessed letters
    attempts = 6  # Number of attempts allowed
    
    print("Welcome to Hangman!")  # Game introduction
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")  # Show current state of word
        print(f"Attempts left: {attempts}")  # Show remaining attempts
        
        guess = input("Guess a letter: ").lower()  # Take user input for a letter
        
        if guess in guessed_letters:
            print("You already guessed that letter!")  # Inform user if letter is already guessed
            continue
        
        guessed_letters.add(guess)  # Add guessed letter to set
        
        if guess in word:
            print("Good job! That letter is in the word.")  # Inform user if guess is correct
        else:
            print("Wrong guess! Try again.")  # Inform user if guess is incorrect
            attempts -= 1  # Reduce attempts on wrong guess
        
        if all(letter in guessed_letters for letter in word):  # Check if all letters are guessed
            print(f"\nCongratulations! You guessed the word: {word}")
            return
    
    print(f"\nGame Over! The word was: {word}")  # If attempts run out, show the correct word

if __name__ == "__main__":
    hangman()  # Start the Hangman game
