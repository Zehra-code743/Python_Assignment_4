def add_numbers(numbers):
    '''
    takes a list of numbers and returs the sums of the numbers

    '''
    total_so_far = sum(numbers)
    return total_so_far

def main():
    '''
    Command line version of summing the numbers

    '''
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        sum_of_numbers = sum(numbers)
        print(f"The sum of the numbers is: {add_numbers(numbers)}")
    except ValueError:
        print("Invalid input. Please enter numbers separated by space.")

if __name__ == "__main__":
    main()