def get_last(lst):
    '''
    Prints the last element of the provided list
    '''
    if lst:  # Ensure the list is not empty
        print('Last element:', lst[-1])
    else:
        print('The list is empty!')

def get_lst():
    '''Prompts the user to enter one element of the list at a time and returns the resulting list'''
    lst = []
    elem = input('Please enter element of the list or press enter to stop: ')

    while elem != '':
        lst.append(elem)
        elem = input('Please enter element of the list or press enter to stop: ')

    return lst

def main():
    lst = get_lst()
    get_last(lst)

if __name__ == '__main__':
    main()
