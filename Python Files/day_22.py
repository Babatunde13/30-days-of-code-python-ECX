def fibonacci(n):
    '''
    A function named fibonacci which uses the idea of recursive programming.

    Parameter: n

    Return: The nth term of the fibonacci sequence
    '''

    if n == 0: # Checks if it is the first element
        return 0
    elif n == 1: # Checks if it is the 2nd element
        return 1
    else: # Recursively gets the nth term
        return fibonacci(n - 1) + fibonacci(n - 2)

