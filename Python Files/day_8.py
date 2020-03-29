def Hangman(secret_word, N):
    '''
    A function named Hangman which tells the user to guess the letters in a text
     and tells the user if they lose or win

    Parameter: secret_word: The word they are to guess it's letters,
     N the number of guesses.

    Returns: win: if the user wins
             lost: if the user loses.

    @author: Babatunde Koiki
    Created on 2020-03-29 
    '''
    for _ in range(N):
        user_guess = input(input('Guess all the letters in the secret word: '))
        if set(secret_word.lower()) == set(user_guess.lower()):
            print(set(secret_word), set(user_guess))
            res = 'won'
        else:
            print(set(secret_word), set(user_guess))
            res = 'lost'

    return res

print(set('babatunde') == set('butaend'))

print(Hangman('Babatunde', 5))