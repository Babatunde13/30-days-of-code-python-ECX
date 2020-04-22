def closest_power(base: int, target: int) -> int:
    """
    This function returns the closest power to raise the base whose result does not exceed target.
    Parameter ---
            base: the base(int) the number we want to find it's closest power to target
            target: int

    Return: an integer, the closest power of base to target whuch baser raise to the power of the value is < target
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
