import random, string

def password_generator(password_lenght):
    '''
    A function named password_generator that takes in the .
     The function generates a password of lenght password_lenght

    Parameter:  password_lenght

    Returns: The generated password and also prints if the password is weak or strong.
    
    @author: Babatunde Koiki
    Created on 2020-03-24 
    '''

    password = ''.join(random.choices(string.ascii_letters+str(1234567890), k=password_lenght)) # Generates a password of lenght password_lenght
    if password_lenght < 8: # Checks if password_lenght is less than 8
        return 'Your pass word is weak'
    
    return password # If condition is False this happens