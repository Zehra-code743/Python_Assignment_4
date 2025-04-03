import random  # Import the random module to shuffle characters
import string  # Import the string module to access letters, digits, and symbols

def generate_password(length=12):
    """Function to generate a random password"""
    if length < 4:
        print("Password length should be at least 4 characters!")  # Ensure a minimum length
        return None
    
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase  # All lowercase letters
    uppercase_letters = string.ascii_uppercase  # All uppercase letters
    digits = string.digits  # All digits (0-9)
    symbols = string.punctuation  # Special characters
    
    # Ensure password has at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password length with random choices from all sets combined
    all_characters = lowercase_letters + uppercase_letters + digits + symbols
    password += random.choices(all_characters, k=length - 4)
    
    random.shuffle(password)  # Shuffle the password to randomize character order
    
    return "".join(password)  # Convert the list to a string and return it

# Main execution block
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))  # Take user input for password length
        password = generate_password(length)  # Generate the password
        if password:
            print(f"Generated Password: {password}")  # Display the generated password
    except ValueError:
        print("Please enter a valid number!")  # Handle invalid input
