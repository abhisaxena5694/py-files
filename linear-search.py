#this function performs a linear search on a list of numbers to search for an element.
def linear_search():
    DATA_LIST = input("Enter a list of numbers:")
    element = input("Enter the element to be searched:")
    flag = 0 # flag indicates whether the 'element' has been found or not; 0 = "NOT FOUND", 1 = "FOUND"
    for i in range(len(DATA_LIST)): #loop for traversing the list to compare 'element' with all the list members.
        if DATA_LIST[i] == element:
            print "Element found at", i + 1, "position."
            flag = 1
            break
    if flag == 0:
        print "Element not found."
        
linear_search()
