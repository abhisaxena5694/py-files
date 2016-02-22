def linear_search():
    DATA_LIST = input("Enter a list of numbers")
    element = input("Enter the element to be searched")
    indicator = 0
    for i in DATA_LIST:
        if DATA_LIST[i] == element:
            print "Element found at", i, "index position."
            indicator = 1
            break
    if indicator == 0:
        print "Element not found."
        
l_search = linear_search()
print l_search
