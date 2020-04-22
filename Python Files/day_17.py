def abundant(n: int) -> bool:
    '''
    A function that checks if a number is abundant
    Parameter: n: int
    Returns: bool, True if n is abundant, otherwise False
    '''
    k = [i if n%i == 0 else 0 for i in range(1,(n//2)+1)]
    k = sum(k)
    if k > n:
        return True
    return False


def sum_abundant(n) -> tuple:
    '''
    A function that first n abundant numbers and their sum
    Parameter: n:int --> number to end in count.
    Returns: the first n abundant numbers in a list and their sum.
    '''
    i, k = 1, []
    while len(k) < n:
        if abundant(i):
            k.append(i)
        i += 1
    return k, sum(k)

print(sum_abundant(7))
