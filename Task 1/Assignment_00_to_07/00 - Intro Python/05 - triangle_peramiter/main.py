def main():
    side = float(input('What is the Length of the Side? '))

    side1 = float(input('What is the Length of the Side2? '))

    side2 = float(input('What is the Length of the Side3? '))

    area = side * side1 * side2

    print(f'The area of the triangle is {area}')


if __name__ == '__main__':
    main()    