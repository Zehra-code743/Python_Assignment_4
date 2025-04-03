Max : int = 3

def short(lst):
    '''
    remove elements from the end of the list until its length is reached to max
    
    '''
    while len(lst) > Max:
     last = lst.pop()
     print('Removed element:', last)


def get():
   '''
   user enter the value of the element one by one and returns the list

   '''
   lst = []
   while True:
      val = input('Enter an element :(or enter to stop )')
      if val == '':
         break
      lst.append(val)
   return lst

def main():
   lst = get()
   print('Original List:', lst)
   short(lst)
   print('Shortened List:', lst)

if __name__ == '__main__':
    main()   



        

        