def captains_room(list_:list) -> str:
    '''
    A function named captain's room which finds the element whose count is 1.

    Parameter: -------------
                list_: list
                        The room numbers of tourist and their captain.
    
    Returns: a string and inserts the value whose count in the room numbers is 1.
    '''
    for val in list_:
        if list_.count(val) == 1:
            return f"The captain's room number is {val}"

print(captains_room([1, 1, 1, 12, 3, 3, 4, 5, 6, 4, 5, 3]))
