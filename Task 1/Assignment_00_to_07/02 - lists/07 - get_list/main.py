def main():
    lst = []

    while True:
        var = input('Please enter your Value :')
        if var == '':
            break
        lst.append(var)
        print('Current List:', lst)

if __name__ == '__main__':
    main()
