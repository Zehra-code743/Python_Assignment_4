def main():
    '''
    Countdown from 10 to 1 with a "liftoff" message after each countdown.'''

    for i in range(10 , 0 ,-1):
        print(i, end=" ")

        print ('liftoff')

if __name__ == '__main__' : main()        