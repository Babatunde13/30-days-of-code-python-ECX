from math import log

def closest_power(base_number, target_number):
    '''
    A function named closest power

    Parameters: base_number and target_number

    Returns: The minimum value of the closest power of the base number to the target number
    
    @author: Babatunde Koiki
    Created on 2020-03-24 
    '''
    return int(log(target_number, base_number))



