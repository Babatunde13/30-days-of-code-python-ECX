from math import log

def closest_power(base_number, target_number):
    '''
    A function named closest power

    Parameters: base_number and target_number

    Returns: The minimum value of the closest power of the base number to the target number
    '''
    return int(log(target_number, base_number))



