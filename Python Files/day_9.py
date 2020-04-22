"""
A function that encrypts a text using the number given. It shifts each letter by the number
e.g. given the text ‘Gvvrk’ and decryption key =-6, the result should be ‘Apple’.
Note that if in counting backward, one has to go before A, we continue from Z.
The same goes for counting beyond Z, we continue from A.
Also, all cases should be retained and all non-alphabets should not be modified.

"""



def decryptor(paragraph: str, key: int) -> int:
    '''
    A function that shifts each cahracter in a text by a particular number:
    Parameter: ------
        paragraph: str, text to be shifted
        key: int, number by whuch text is shifted.

    Return: 
        a new text that has been decrypted.
    '''
    #defining a variable for all alphabets in lowercase and uppercase
    lowcase = 'abcdefghijklmnopqrstuvwxyz'
    uppcase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #intializing an empty string for the decrypted paragraph
    decrypted = ''
    paragraph=paragraph.replace("'",'\'')
    
    try:
        # when key is a negative number
        if key < 0:
            for letter in paragraph:
                if letter in lowcase:
                    decrypting = lowcase.index(letter) + key
                    decrypt = lowcase[decrypting]
                    decrypted += decrypt

                elif letter in uppcase:
                    decrypting = uppcase.index(letter) + key
                    decrypt = uppcase[decrypting]
                    decrypted += decrypt

                else:
                    decrypted += letter

        elif key > 0:
            for letter in paragraph:
                if letter in lowcase:
                    decrypting = lowcase.index(letter) + key
                    if decrypting>len(lowcase):
                        decrypt = lowcase[decrypting-26]
                        decrypted += decrypt
                    elif decrypting==len(lowcase):
                        decrypt = lowcase[0]
                        decrypted += decrypt
                    else:
                        decrypt = lowcase[decrypting]
                        decrypted += decrypt
        
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

    except Exception as e:
        return 'Error Message: ', e
    else:
        return decrypted

#invoking the function
print(decryptor('Rcb mjh 9 xo cqn 30 mjhb xo lxmn lqjuunwpn!!','b'))

