def closest_power(base, target):
    """This function returns the closest power to raise the base whose result does not exceed target."""
    #I will use length of list to control the output
    a = []
    #initial power is set at zero
    n = 0
    #Control the running of the loop
    while pow(base,n) <= target:
        a.append(pow(base,n))
        n +=1 #This increases power(n) till the required n is reached (as set in the loop)

    #return the length of the loop but subtract 1: this is because the loop start with power of zero
    #list will append power of 0,1,2,3,... this is why we need to subtract 1 from length of list a. You may start n with 1 as another way
    power = len(a)-1
    
    return power

print(closest_power(2, 63))
