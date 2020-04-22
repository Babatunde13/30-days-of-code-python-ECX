def compressor(tuple_: tuple) -> tuple:
    """
    A function to count the number of occurences of an element in a tuple
    
    Returns a tuple of tuple.
    """
    list_ = list(tuple_) #convert the tuple to list
    count_list = list(set(list_)) #convert the list to a set containing unique elements
    count_list.sort() #sort the list in ascending order
    tuple_list = []
    
    for i in range(len(count_list)):
        count = list_.count(count_list[i])
        tuple_list.append((int(count_list[i]), count))
        
    return tuple(tuple_list)

print(compressor((1, 1, 2, 3, 4, 1, 4, 2)))