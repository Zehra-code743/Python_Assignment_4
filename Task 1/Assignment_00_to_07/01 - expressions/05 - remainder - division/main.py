def main():
    '''
    Command line of division calculator

    '''
    try:
        divide = int(input('plz inter a intiger to divide :'))
        divisor = int(input('plz inter a intiger to divide by :'))
        


        if divisor == 0:
            print('Error: Division by zero is not allowed')
            return
        
        quotient = divide // divisor
        remainder = divide % divisor
        print(f'Quotient: {quotient}, Remainder: {remainder}')
    except ValueError:
        print('Error: Please enter valid integers')

if __name__ == '__main__':
    main()
