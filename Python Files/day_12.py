def Validator(email):

    '''This function receives a email address as string and returns the validity
    '''
    count_a = 0
    dot = email.rfind('.')
    at = email.rfind('@')

    someone = email[0:at]
    example = email[at+1:dot]
    top_domain = email[dot+1:]

    if someone.islower()==True and someone.isascii()==True  or '.' in someone:
        count_a+=1

    if example.islower()==True and example.isalnum()==True or '-' in example :
        count_a+=1
    dot_ = example.find('.')
    if '.' in example and (len(example[dot_+1:dot])==2 or len(example[dot_+1:dot])==3):
        count_a+=1
    if top_domain.isalpha()==True and (len(top_domain)== 2 or len(top_domain)==3):
        count_a+=1

    if count_a == 3 or count_a == 4:
        return 'Valid Email address!'
    else:
        return 'Invalid Email address!'
    
    
    





print(Validator("jan.eadesanya04@gmail.com"))
print(Validator('sowunmi1994@unilag.edu.ng'))
print(Validator('akande&fola@g-mail.com'))
print(Validator('Amala@ewedu.village'))
print(Validator('ecxunilag@yahoo.co.uk'))
