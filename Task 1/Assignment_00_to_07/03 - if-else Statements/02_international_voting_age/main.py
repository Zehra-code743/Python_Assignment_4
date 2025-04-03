David_age = 17
lily_age = 20
carter_age = 21

def main():

    user = int(input('How old are you?'))

    if user >= David_age:
        print('David is younger than you')
    elif user == David_age:
        print('You are the same age as David')
    else:
        print('David is older than you')

        if user >= lily_age:
            print('Lily is younger than you')
        elif user == lily_age:
            print('You are the same age as Lily')
        else:
            print('Lily is older than you')

            if user >= carter_age:
                print('Carter is younger than you')
            elif user == carter_age:
                print('You are the same age as Carter')
            else:
                print('Carter is older than you')

if __name__ == "__main__":
    main()