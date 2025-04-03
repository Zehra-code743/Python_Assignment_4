def user_number():

    user = []
    while True:
        num = int(input("Enter a number: "))
        if num == '':
            break
        try:
            val = int(num)
            user.append(val)
            print(f"You have entered: {user}")
        except ValueError:
            print("Invalid input. Please enter a number.")
        return user


def count_number(num):
    num_dict = {}
    for i in num:
        num_dict[i] = num_dict.get(i,0) + 1
        return num_dict
    
def print(num_dict):
    for num ,count in num_dict.items():
        print(f"{num}: {count}")



def main():
    user_input = user_number()
    count_dict = count_number(user_input)
    print(count_dict)
    

if __name__ == "__main__":
    main()