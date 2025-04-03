def main():
    fruits = {
        'apple': 1,
        'banana': 2,
        'orange': 3,
        'grape': 4,
        'mango': 5,
        'kiwi': 6,
        'pear': 7,
        'cherry': 8,
        'melon': 9,
        'watermelon': 10
    }

    total = 0
    for fruit, quantity in fruits.items():
        amount = int(input(f'How many {fruits} do you want to buy? '))
        total += quantity * amount

    print(f'Total amount: {total}')
    print('Thank you for shopping!')
    print('Goodbye!')

    if __name__ == '__main__':
        main()