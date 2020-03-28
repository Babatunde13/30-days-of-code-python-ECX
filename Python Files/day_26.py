def GPA_calculator(scores, units):
    '''
    A function named GPA_calculator which computes the GPA of a student

    Parameter: scores - The score of the student
            units: The units of each course
        
    Returns: The GPA of the student.
    '''
    
    grades = []
    for grade in scores: # Loops thriugh all the scores obtained the student
        if grade >= 70: # Checks if the score is an A
            grades.append(5)
        elif grade >= 60: # Checks if the score is a B
            grades.append(4)
        elif grade >= 50: # Checks if the score is a C
            grades.append(3)
        elif grade >= 45: # Checks if the score is an D
            grades.append(2)
        elif grade > 39: # Checks if the score is an E
            grades.append(1)
        else: # Checks if the score is F
            grades.append(0)

    # Computes the sum of product of every element in grades and units list and divides by sum of units.
    return sum([grade * unit for grade, unit in zip(grades, units)])/sum(units)




