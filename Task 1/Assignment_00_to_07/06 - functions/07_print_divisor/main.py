def print_divisors(num):
    """Prints the divisors, quotients, and remainders of the given number."""
    print(f'Here are the divisors of {num}:')

    for i in range(1, num + 1):
        if num % i == 0:
            print(f'Divisor: {i}')
            print(f'Quotient: {num // i}')
            print(f'Remainder: {num % i}')
            print('-' * 20)  # Separator for readability

def main():
    user_input = int(input('Enter a number: '))
    print_divisors(user_input)  # No need to print its return value

if __name__ == "__main__":
    main()
