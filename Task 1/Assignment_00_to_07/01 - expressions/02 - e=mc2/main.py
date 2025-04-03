def calculate(mass):
    C = 299792458

    return mass * (C ** 2)

def main():
    '''
    Command line version of mass energy calculation

    '''

    try:
        mass = float(input('Enter mass: '))
        print('e = m * C^2...')
        print(f'm = {mass} kg')
        print(f'C = {299792458} m/s')
        print(f'{energy} is equal to Energy')

        
    except ValueError:
        print('Invalid input')
        return

    energy = calculate(mass)

    print(f'Energy: {energy} J')

if __name__ == '__main__':
    main()
