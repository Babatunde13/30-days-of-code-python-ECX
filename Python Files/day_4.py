def is_Nigerian(phone_number):
    '''
    A function named is_Nigerian which validate a Nigerian phone number

    Parameter: phone_number, which is a string with or without country code

    Returns: True if number is a Nigerian number False otherwise.
    @author: Babatunde Koiki
    Created on 2020-03-24 
    '''

    if phone_number[1:].isnumeric(): # Checks if all characters except the first which can be `+` are number.
        if (phone_number[:4] == '+234' and len(phone_number) == 14) and (phone_number[4:6] == '81' or phone_number[4:6] == '80' or phone_number[4:6] == '70' or phone_number[4:6] == '90'): #Checks if number starts with +234 and lenght is 14.
             # and  Checks if one of 80, 81, 90, 70 are immediately after the country code.
            return True
            
        elif (phone_number[:3] == '080' or phone_number[:3] == '081' or phone_number[:3] ==  '070' or phone_number[:3] == '090') and len(phone_number) == 11: # Checks if number starts with one of 080, 081, 070, 090 and lenght of number is 11
            return True
        return False # If any of these two condition are  not met, it returns False
    return False # If number contains non numeric characters except +, it returns False

     