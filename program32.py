items = input("enter the elements of list").split()   #.split() turns it into a list of items, which is what you want when checking for "list is empty or not".

if len(items) == 0 :
    print("the list is empty")
else :
    print("the list is not empty")    