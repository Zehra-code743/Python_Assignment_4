import time  # Import the time module to use sleep function

# Function to run the countdown timer
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert total seconds to minutes and seconds
        timer = f'{mins:02}:{secs:02}'  # Format the timer as MM:SS
        print(timer, end='\r')  # Overwrites the previous output to show updated time
        time.sleep(1)  # Pause for 1 second
        seconds -= 1  # Decrease the countdown timer by 1 second
    
    print("\nTime's up! ⏰")  # Print message when countdown reaches zero

# Main execution block
if __name__ == "__main__":
    try:
        seconds = int(input("Enter countdown time in seconds: "))  # Take user input for countdown time
        countdown_timer(seconds)  # Start the countdown
    except ValueError:
        print("Please enter a valid number!")  # Handle invalid inputs
