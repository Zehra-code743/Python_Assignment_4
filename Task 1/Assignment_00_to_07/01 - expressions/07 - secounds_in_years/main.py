Days_per_Years = 365
Hours_per_Day = 24
Minutes_per_Hour = 60
Seconds_per_Minute = 60

def calculate ():
    '''
Calculates the number of seconds in a year

'''

    return Days_per_Years * Hours_per_Day * Minutes_per_Hour * Seconds_per_Minute

def main():
    secounds = calculate()
    print(f'There are {secounds} seconds in a year.')


if __name__ == '__main__':
    main()
