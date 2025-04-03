def add_copies(my_list , data):
    '''
    Add three copies of data to the provided list

    '''
    for _ in range(3):
        my_list.append(data)

def main():
    massage = input('Enter a massage to copy :')
    my_list = []        

    print('List before :',my_list)
    add_copies(my_list , massage)

    print('List after :',my_list)

if __name__ == '__main__':
    main()    