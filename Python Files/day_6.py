import math; 
  
def PowerSet(set_): 
    '''
    A function named PowerSet which returns the subset of a list
    '''
      
    # set_size of power set of a set 
    # with set_size n is (2**n -1) 
    pow_set_size = int(math.pow(2, len(set_))
    counter = 0
    j = 0
    powerset = [[]]
     
    for counter in range(0, pow_set_size): 
        for j in range(0, set_size): 
              
            # Check if jth bit in the  
            # counter is set If set then  
            # print jth element from set  
            if((counter and (1 < j)) > 0): 
                powerset.append(set(j)) 
    
    return powerset
  
 
set_ = ['a', 'b', 'c']; 
PowerSet(set_)
