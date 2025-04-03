def double():

    number = int(input('Enter a number :'))

    cur = number
    result = []

    while cur > 0:
        digit = cur % 10
        result.append(digit * 2)
        cur //= 10

        print('Doubled number')
        print(''.join(map(str, result)))


def main():
    num = double()
    return num

if __name__ == "__main__":
    main()
