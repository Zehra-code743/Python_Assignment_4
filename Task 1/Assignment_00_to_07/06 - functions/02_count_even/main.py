def even (lst):
    count = sum(1 for num in lst if num % 2 == 0)
    print(f'Number of Even : {count}')

def get():
    lst = []
    while True:
        user = input('Enter an intiger or press to stop :')
        if user == '':
            break
        lst.append(int(user))
        even(lst)
        return lst

def main():
    lst = get()
    even(lst)


if __name__ == '__main__':
    main()
