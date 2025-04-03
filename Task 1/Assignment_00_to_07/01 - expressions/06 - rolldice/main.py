import random

Num_Sides = 6

def roll_dice():
    '''
    Simulates a Rolling dices and prints thier Total Number

    '''
    dice_1 = random.randint(1, Num_Sides)
    dice_2 = random.randint(1, Num_Sides)

    total = dice_1 + dice_2

    print(f'Dice have {Num_Sides} sides each')
    print(f'Firt die : {dice_1}')
    print(f'Second die : {dice_2}')
    print(f'Total number : {total}')

def main():
    roll_dice()

if __name__ == '__main__':
    main()        