def multiple(message, repeats):
    """
    This function repeats a given message a specified number of times.
    """
    for _ in range(repeats):
        print(message)

def main():
    message = input('Please type a message: ')
    repeats = int(input('How many times do you want to repeat the message? '))
    multiple(message, repeats)

if __name__ == "__main__":
    main()
