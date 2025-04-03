def main():
    """
    This function takes a number as input and doubles it until it reaches 100.
    """
    value = int(input('Enter a Number : '))

    while value < 100:
        value = value * 2
        print(value ,end=' ')

if __name__ == '__main__':
    main()


