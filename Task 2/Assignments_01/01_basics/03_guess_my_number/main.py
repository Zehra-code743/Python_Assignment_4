import random 

def main():
    """
    This is a simple number guessing game.
    The user has to guess a secret number between 1 and 100.
    """
    secret_number :int = random.randint(1, 100)

    guess = int(input('Enter a secret number :'))

    while guess != secret_number:
        if guess < secret_number:
            print('Too low! Try again.')
        else:
            print('Too high! Try again.')

            guess = int(input('Enter a secret number :'))
            print('Great guess! The number was :',secret_number)


if __name__ == "__main__":
    main()