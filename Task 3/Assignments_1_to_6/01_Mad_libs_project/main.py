# Function to play the Mad Libs game
def madlibs():
    """
    This function asks the user for words and inserts them into a story template.
    """
    
    # Taking user inputs for different words
    noun = input("Enter a noun: ")  # Ask for a noun
    verb = input("Enter a verb: ")  # Ask for a verb
    adjective = input("Enter an adjective: ")  # Ask for an adjective
    place = input("Enter a place: ")  # Ask for a place
    
    # Creating the Mad Libs story template
    story = f"One day, a {adjective} {noun} decided to {verb} at {place}. It was an unforgettable adventure!"
    
    # Display the completed story
    print("\nHere is your Mad Libs story:")
    print(story)

# Main execution block
if __name__ == "__main__":
    madlibs()  # Call the Mad Libs function to start the game
