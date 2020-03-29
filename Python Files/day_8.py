def Hangman(secret_word, N):
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