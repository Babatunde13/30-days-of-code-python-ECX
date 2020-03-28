
 

def binary_adder(bin_1, bin_2):
    '''
    The function named binary_adder

    Parameters: bin_1 and bin_2. The parameters are both in binary

     Returns the sum of the two parameters in binary
    '''

    return int(bin(int('0b'+str(bin_1), 2) + int('0b'+str(bin_2), 2))[2:])

