import random

def main():
    secret = random.randint(1, 100)

    guess = int(input('Enter a secret number :'))

    while guess != secret:
        if guess < secret:
            print('Too low! Try again.')
        else:
            print('Too high! Try again.')

        guess = int(input('Enter a secret number :'))

    print('Great guess! The number was :',secret)

    play_again = input('Do you want to play again? (yes/no) :').lower()
    while play_again == 'yes':
        main()
        play_again = input('Do you want to play again? (yes/no) :').lower()
        if play_again != 'yes':
            print('Thank you for playing!')

if __name__ == '__main__':
    main()