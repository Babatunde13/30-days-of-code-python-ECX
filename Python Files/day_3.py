def bin_search(list_, num):
    '''
    A function named bin_search. The functions
     searches list_ and checks if num is in ut using the concept of binary search, you can   
      use this link to read more on binary https://en.wikipedia.org/wiki/Binary_search_algorithm

    Parameters:  list_ and num

    Returns True if num is in list_ else False.
    '''

    list_.sort() # Ensures that the list is sorted
    no = len(list_)//2 # The index of the median element in the list
    while len(list_) > 0:
        if num == list_[no]: # Checks if the number is the median value
            return True
        elif num > list_[no]: # Check if the number is greater than the median value
            for val in list_[no:]: # Searches for the number in the upper half of the list.
                if val == num:
                    return True
                
        elif num < list_[no]: # Check if the number is less than the median value
            for val in list_[:no]: # Searches for the number in the upper half of the list.
                if val == num:
                    return True 
        
        return False # Returns False if all of the condition above are not true. 
    
    return False # Return False if list is empty.
