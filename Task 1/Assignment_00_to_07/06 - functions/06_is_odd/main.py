def odd(value)-> bool:
    return value

def main():
    num = int(input("Enter a number: "))
    for i in range(10 , 20):
        if odd(i):
            print(i)
        else:
            (f'{i} even')    


if __name__ == "__main__":
    main()