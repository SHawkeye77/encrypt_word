"""
Samuel Hohenshell

Contains Vigenére cipher code
"""

# Given an encryption key and unencrypted letter, return the 
#  Vigenere cipher equivalent of it
# NOTE: We assume the string is all caps
def encrypt(string, key):
    cipher_text = []
    for i in range(len(string)):
        if string[i].isalpha():
            new_letter = (ord(string[i]) + ord(key[i])) % 26
            new_letter += ord('A') 
            cipher_text.append(chr(new_letter))
        else:
            cipher_text.append(string[i])
    return("".join(cipher_text))

# Given a decryption key and encrypted string, return associated plaintext
# NOTE: We assume the string is all caps
def decrypt(string, key): 
    plain_text = [] 
    for i in range(len(string)): 
        if string[i].isalpha():
            letter = (ord(string[i]) - ord(key[i]) - 26) % 26
            letter += ord('A') 
            plain_text.append(chr(letter)) 
        else:
            plain_text.append(string[i])
    return("".join(plain_text)) 


def lengthen_key(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
