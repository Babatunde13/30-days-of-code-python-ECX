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
    res = '
    for _ in range(N):
        user_guess = input(input('Guess a the letter in the secret word: '))
        if user_guess.lower() in secret_word.lower():
            print('corrct guess')
            res += user_guess
        else:
            print('Invalid guess')
            
    if user_guess.lower() == res.lower():
        return 'Won'
    return 'Lost'


print(Hangman('Babatunde', 5))
