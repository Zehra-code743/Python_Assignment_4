import random  # Import the random module to let the computer make a random choice

def get_computer_choice():
    """Function to get the computer's choice"""
    choices = ['rock', 'paper', 'scissors']  # List of possible choices
    return random.choice(choices)  # Return a random choice from the list

def determine_winner(player, computer):
    """Function to determine the winner based on player and computer choices"""
    if player == computer:
        return "It's a tie!"  # If both choose the same, it's a tie
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"  # Winning conditions for the player
    else:
        return "Computer wins!"  # If none of the above, computer wins

def rock_paper_scissors():
    """Main function to play the Rock, Paper, Scissors game"""
    print("Welcome to Rock, Paper, Scissors!")  # Introduction message
    
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()  # Get player input
        
        if player_choice == 'quit':
            print("Thanks for playing! Goodbye!")  # Exit message
            break  # Exit the loop
        
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter rock, paper, or scissors.")  # Handle invalid input
            continue  # Restart loop
        
        computer_choice = get_computer_choice()  # Get the computer's choice
        print(f"Computer chose: {computer_choice}")  # Display computer's choice
        
        result = determine_winner(player_choice, computer_choice)  # Determine the winner
        print(result)  # Display the result

# Main execution block
if __name__ == "__main__":
    rock_paper_scissors()  # Start the game
