import random 

def main():
    n_number = 10
    min_value = 1
    max_value = 100

    random_numbers = [random.randint(min_value, max_value) for _ in range(n_number)]

    print(f"Random numbers between {min_value} and {max_value}: {random_numbers}")
    print(f"Sum of all random numbers: {sum(random_numbers)}")

if __name__ == "__main__":
    main()    