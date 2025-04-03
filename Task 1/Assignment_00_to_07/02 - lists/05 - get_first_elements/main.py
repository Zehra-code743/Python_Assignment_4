def get_first(lst):
    '''
    prints the first element of a provided list
    
    '''
    print(lst[0])


def get_list():
    '''
    prompts the user to enter one element of the list at time and return result of the list

    '''
    lst = []
    elem = input('please enter an element of the list or press enter to finish : ')



    while elem != '':
        lst.append(elem)
        elem = input('please enter an element of the list or press enter to finish : ')

    return lst

def main():
    lst = get_list()
    get_first(lst)


if __name__ == '__main__':
    main()