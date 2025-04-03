Inches_in_Foot :int = 12

def main():
    '''
    Command line version of feet to inches converter
    
    '''
    try:
        feet = float(input('Enter number of feet : '))
        inches = feet * Inches_in_Foot
        print(f'{feet} feet = {inches} inches')
    except ValueError:
        print('Invalid input. Please enter a numeric value.')


if __name__ == '__main__':
    main()
