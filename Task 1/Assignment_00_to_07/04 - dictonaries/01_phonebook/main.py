def read_number():
    phonebook = {}
    while True:
        name = input('Enter a name: ')
        if name == '':
            break
        number = input('Enter a number: ')
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    for name, number in phonebook.items():
        print(f'{name}: {number}')


def lookup_phonebook(phonebook):
    name = input('Enter a name: ')
    if name in phonebook:
        print(f'{name}: {phonebook[name]}')
    else:
        print(f'{name} is not in the phonebook.')
       

def main():
    phonebook = read_number()
    print_phonebook(phonebook)
    lookup_phonebook(phonebook)

if __name__ == "__main__":
    main()