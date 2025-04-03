def main ():
    """
    prompts the user to enter their name and returns it"
    """
    first = input('Enter your first name :')
    last = input('Enter your last name :')

    email = input('Enter your email address :')

    return f'{first} {last} <{email}>'


print(main()) # Call the main function and print the returned value.