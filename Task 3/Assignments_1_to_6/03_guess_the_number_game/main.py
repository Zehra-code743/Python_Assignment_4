import random  # Import the random module to generate a random number

def number_guessing_game():
    """Function to play the number guessing game"""
    number_to_guess = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Initialize the number of attempts
    
    print("Welcome to the Number Guessing Game!")  # Introduction message
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))  # Ask the user for a number
            attempts += 1  # Increment the attempt counter
            
            if guess < number_to_guess:
                print("Too low! Try again.")  # Hint if guess is too low
            elif guess > number_to_guess:
                print("Too high! Try again.")  # Hint if guess is too high
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Invalid input! Please enter a number.")  # Handle non-numeric input

# Main execution block
if __name__ == "__main__":
    number_guessing_game()  # Start the game
