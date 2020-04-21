def desc_triangle(a, b, c):
    '''
    A function named desc_triangle

    Parameters: a, b and c, the lenght of each size of the triangle.

    Returns: The type of triangle and the value of it's area
    '''

    # Using Hero's Formula 
    s = (a + b + c) / 2
    area = (s * (s-a) * (s - b) * (s - c)) ** 0.5

    if a == b == c: # Checks if all sides are equal
        return "Equilateral Triangle", area

    elif a == b or a == c or b == c: # Checks if any two sides are equal
        return "Iscocelles Triangle", area

    else: # If first two are False, then triangle is a scalene triangle.
        k = sorted([a, b, c])
        if k[0] ** 2 + k[1] ** 2 == k[2] ** 2:
            return "Right andled Scalene triangel", area
        return "Scalene Triangle", area
