def closest_power(base: int, target: int) -> int:
    """
    This function returns the closest power to raise the base whose result does not exceed target.
    Parameter ---
            base: the base(int) the number we want to find it's closest power to target
            target: int

    Returns: The minimum value of the closest power of the base number to the target number
    
    @author: Babatunde Koiki
    Created on 2020-03-24
    """
    
    a = []
    #initial power is set at zero
    n = 0
    #Control the running of the loop
    while base ** n <= target:
        a.append(base ** n)
        n +=1 #This increases power(n) till the required n is reached (as set in the loop)
    
    return len(a)-1

print(closest_power(2, 63))
