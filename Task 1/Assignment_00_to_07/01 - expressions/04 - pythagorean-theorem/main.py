import math

def main():
    '''
    Command line version of pythagoren Calculator
    
    '''

    # Get user input
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    # Calculate the length of the hypotenuse
    hypotenuse = math.sqrt(a**2 + b**2)

    # Print the result
    print("The length of the hypotenuse is:", hypotenuse)
    print("The calculated area of the triangle is:", 0.5 * a * b)

if __name__ == "__main__":
    main()