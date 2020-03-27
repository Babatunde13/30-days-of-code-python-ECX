def bin_search(list_, num):
    '''
    A function named bin_search which takes in two parameters list_ and num. The functions
     searches list_ and checks if num is in ut using the concept of binary search, you can   
      use this link to read more on binary https://en.wikipedia.org/wiki/Binary_search_algorithm

    Returns True if num is in list_ else False.
    '''

    list_.sort() # Ensures that the list is sorted
    no = len(list_)//2 # The index of the median element in the list
    if num == list_[no]: # Checks if 
        return True
    elif num > list_[no]:
        for val in list_[no:]:
            if val == num:
                return True
            
    elif num < list_[no]:
        for val in list_[:no]:
           if val == num:
                return True 
    
    return False
