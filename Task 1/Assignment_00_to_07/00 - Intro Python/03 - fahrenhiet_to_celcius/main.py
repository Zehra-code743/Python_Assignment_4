def main():
    fehrenhiet = float(input('Enter Temprature in Fehrenhiet : '))

    celsius = (fehrenhiet - 32) * 5.9 /9.0

    print(f'Temprature :{fehrenhiet} F = {celsius} C')

if __name__ == '__main__':
    main()
