def guessing_game(no_of_guess, target):
    '''
    A function named guessing_game that takes in two parameters no_of_guesses and target,
     it asks for the user guess and prints your guess is higher or lower. This is repeated by
     the no_of_guess.day2.py

    Returns: the positive difference between the final guess and the correct value
    '''

    for num in range(no_of_guess):
        yournum = int(input('Enter a number: '))
        if yournum > target:
            print('Your guess is higher than the correct number')
        elif yournum < target:
            print('Your guess is lower than the correct number')
        else:
            print('Your guess is equal to the correct number')
            break
    return abs(target - yournum)