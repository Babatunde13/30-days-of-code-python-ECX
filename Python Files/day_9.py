"""
A function that encrypts a text using the number given. It shifts each letter by the number
e.g. given the text ‘Gvvrk’ and decryption key =-6, the result should be ‘Apple’.
Note that if in counting backward, one has to go before A, we continue from Z.
The same goes for counting beyond Z, we continue from A.
Also, all cases should be retained and all non-alphabets should not be modified.

"""

#defining a variable for all alphabets in lowercase and uppercase
lowcase = 'abcdefghijklmnopqrstuvwxyz'
uppcase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decryptor(paragraph, key):
    
    #intializing an empty sting for the decrypted paragraph
    
    decrypted = ''
    
    paragraph=paragraph.replace("'",'\'')
    
    try:
        # when key is a negative number
        if key < 0:
                #Looping through the alphabets in the paragraph
            for letter in paragraph:
                
                #checking if the alphabet is lowercase
                if letter in lowcase:
                    
                    #getting the index of the alphabet and subtracting the key to make it count backward
                    decrypting = lowcase.index(letter) + key
                    #getting the value of the calculated index
                    decrypt = lowcase[decrypting]
                    #adding it to the originally created decrypted string
                    decrypted += decrypt
                    
                #if letter is uppercase
                elif letter in uppcase:
                    decrypting = uppcase.index(letter) + key
                    decrypt = uppcase[decrypting]
                    decrypted += decrypt
                else:
                    decrypted += letter
                    
        #when key is a positive number
        elif key > 0:

            for letter in paragraph:
                if letter in lowcase:
                    decrypting = lowcase.index(letter) + key
                    if decrypting>len(lowcase):
                        #handling scenerius where caluculated index is greater than 26
                        decrypt = lowcase[decrypting-26]
                        decrypted += decrypt
                        #handling cases where calculated index is 0
                    elif decrypting==len(lowcase):
                        decrypt = lowcase[0]
                        decrypted += decrypt
                    else:
                        decrypt = lowcase[decrypting]
                        decrypted += decrypt
                #doing the same for uppoercase letters
                elif letter in uppcase:
                    decrypting = uppcase.index(letter) + key
                    if decrypting>len(lowcase):
                        decrypt = uppcase[decrypting-26]
                        decrypted += decrypt
                    elif decrypting==len(lowcase):
                        decrypt = lowcase[0]
                        decrypted += decrypt
                    else:
                        decrypt = uppcase[decrypting]
                        decrypted += decrypt
                else:
                    decrypted += letter
    #handling exception
    except Exception as e:
        print('Error Message: ', e)
    print(decrypted)

#invoking the function
print(decryptor('Rcb mjh 9 xo cqn 30 mjhb xo lxmn lqjuunwpn!!','x'))

