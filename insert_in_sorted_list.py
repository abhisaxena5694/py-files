"""This function asks the user for a sorted list of numbers and a number to be inserted in the list. 
It then returns a new sorted list with the number inserted in its appropriate position."""
def insert_in_sorted_list():
    DATA_LIST = input("Enter a sorted list of numbers:")
    element = input("Enter the number to be inserted:")
    if type(DATA_LIST) != list:
        DATA_LIST = list(DATA_LIST)
    list_length = len(DATA_LIST)
    for index in range(list_length):
        if element > DATA_LIST[index]:
            position = index + 1
        #else: 
        #    continue
    count = list_length
    DATA_LIST.append(None)
    while count >= position:
        DATA_LIST[count] = DATA_LIST[count - 1]
        count -= 1
    DATA_LIST[position] = element
    return DATA_LIST
   


# testing command
print "Your new list is:", insert_in_sorted_list()
