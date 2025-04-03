# Corrected variable type hinting
Prompt: str = 'What do you want to do?'
Joke: str = '''Here is the joke: Why did the scarecrow win an award?
Because he was outstanding in his field! 🌾😆'''
Sorry: str = "Sorry, I don't understand. Please try again."

def main():
    """
    This function gets the user's input, processes it, and returns a response.
    """
    user = input('Enter your prompt: ').strip().lower()  # Trim spaces and lowercase input

    if user == Prompt.lower():  # Compare lowercase versions
        print(Joke)
    else:
        print(Sorry)

if __name__ == '__main__':
    main()
