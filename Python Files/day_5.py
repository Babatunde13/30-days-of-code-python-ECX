def faithful(number):
    '''
    A function named faithful which computes the nth faithful number

    Parameter: number, twhich is used in computing numberth term of the faithful sequence

    Return: Returns the nth term of the faaithful sequence

    @author: Babatunde Koiki
    Created on 2020-03-29 
    '''
    number = bin(number)[2:] # Converts the number to binary and turns it into a string
    res = [] # Creates an empty list where the sum of it's element after computation is the nth term
    x = 0 # Initialises x to 0, where x is the power in each case
    for n in number[::-1]: # Loops through the reverse of the binary
        res.append(int(n) *( 7 ** x)) 
        x = x+1 # Adds 1 to the power, x
        
    return sum(res) # returns the sum of the list.
    


