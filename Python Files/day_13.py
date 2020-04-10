def wrapper(para,n):
    """
    This function takes in a paragraph as a string and
    aximum number of characters as an integer
    
    Returns the wrapped text as a string
    
    Created on Tue Apr  7 11:02:34 2020

    @author: Babatunde Koiki
    """
    new_text = para.split("\n")
    final=[]
    for each in new_text:
        final.append('\n'.join(each[i:i+n] for i in range(0,len(each),n)))
    return '\n'.join(final)
