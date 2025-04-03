Height = 50

def main():
    while True:
        height = int(input("Enter your height in cm: "))
        if height >= Height:
            print("You are tall enough to ride!")
            break
        else:
            print("You need to grow some more to ride.")

if __name__ == "__main__":
    main()