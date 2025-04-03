def in_range(n:int ,low: int ,high: int)->bool:
    return low <= n <= high

def main():
    num = int(input("Enter a number: "))
    low = int(input("Enter the lower limit: "))
    high = int(input("Enter the upper limit: "))
    if in_range(num, low, high):
        print(f"{num} is within the range of {low} and {high}.")

if __name__ == "__main__":
    main()