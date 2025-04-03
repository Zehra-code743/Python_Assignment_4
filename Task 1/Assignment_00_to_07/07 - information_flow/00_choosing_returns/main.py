Age = 18

def adult(age):
    return age >= Age

def main():
    age = int(input("Enter your age: "))
    if adult(age):
        print("You are an adult")
    else:
        print("You are not an adult")

if __name__ == "__main__":
    main()
