def main():
    AFFIRMATION = "I'm capable of doing anything that I learn and put on my mind.\n\n"

    print("Please enter your following information:")
    print(AFFIRMATION)

    user_feedback = ""  # Initialize before the loop

    while user_feedback != AFFIRMATION.strip():
        user_feedback = input("Please enter your feedback: ").strip()
        if user_feedback != AFFIRMATION.strip():
            print("\nThat was not the affirmation. Try again.")
            print(AFFIRMATION)
        else:
            print("Wow! That's absolutely awesome and correct!")

if __name__ == "__main__":
    main()
