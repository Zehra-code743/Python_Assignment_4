def stock(friuts):
    inventory = {
        'apple': 100,
        'banana': 50,
        'orange': 75
    }
    return inventory.get(friuts.upper())

def main():
    friuts = input("Enter the name of the fruit: ")
    quantity = stock(friuts)
    if quantity is None:
        print(f"No stock available for {friuts.capitalize()}")
        return
    print(f"The current stock of {friuts.capitalize()} is {quantity}")
    print("Thank you for using our fruit shop!")
    return

if __name__ == "__main__":
    main()