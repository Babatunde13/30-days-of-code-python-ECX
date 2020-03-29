def GPA_calculator(scores, units):
    '''
    A function named GPA_calculator which computes the GPA of a student

    Parameter: scores - The score of the student
            units: The units of each course
        
    Returns: The GPA of the student.
    @author: Babatunde Koiki
    Created on 2020-03-24 
    '''
    
    grades = []
    for grade in scores: # Loops thriugh all the scores obtained the student
        if grade >= 70:  grades.append(5) # Checks if the score is an A
           
        elif grade >= 60: grades.append(4)# Checks if the score is a B
            
        elif grade >= 50: grades.append(3)# Checks if the score is a C
            
        elif grade >= 45: grades.append(2) # Checks if the score is an D
            
        elif grade > 39: grades.append(1) # Checks if the score is an E
        
        else: grades.append(0)# Checks if the score is F
            
    # Computes the sum of product of every element in grades and units list and divides by sum of units.
    return sum([grade * unit for grade, unit in zip(grades, units)])/sum(units)




