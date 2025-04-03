def average(a: float, b: float) -> float:
    """
    Function to calculate the average of two numbers."
    """
    return (a + b) / 2

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = average(num1, num2)
    print(f"The average of {num1} and {num2} is: {result}")
    return result

if __name__ == "__main__":
    main()