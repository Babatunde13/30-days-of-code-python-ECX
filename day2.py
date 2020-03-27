import random, string

def password_generator(password_lenght):
    '''
    A function named password_generator that takes in the parameter password_lenght.
     The function generates a password of lenght password_lenght

    Returns: The generated password and also prints if the password is weak or strong.
    '''

    password = ''.join(random.choices(string.ascii_letters+str(1234567890), k=password_lenght))
    if password_lenght < 8:
        return 'Your pass word is weak'
    
    return password