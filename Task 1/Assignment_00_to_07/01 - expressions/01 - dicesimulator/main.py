import random

Num_Sides = 6

def roll_dice():
    '''
    Simulates a Rolling dices and prints thier Total Number

    '''

    dice_1 = random.randint(1, Num_Sides)
    dice_2 = random.randint(1, Num_Sides)

    total = dice_1 + dice_2

    print("You rolled a " + str(dice_1) + " and a " + str(dice_2) + " for a total of " + str(total))

def main():
    dice_1 = 10

    print (f'dice_1 = {dice_1}')

for i in range(3):
    roll_dice()


if __name__ == "__main__":
    main()
