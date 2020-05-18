"""
Samuel Hohenshell

Given a user-inputted ciphertext and key, this will decript it.
This will specifically work with the encryption used in invis_ink.py.
"""

import vigenere

def main():

    # Gathering user input
    key = input("Input cypher key: ").strip()
    while True:
        text = input("Input text to decode: ").strip()

        # Printing deciphered text and returning
        print("Deciphered text:")
        print(vigenere.decrypt(text, vigenere.lengthen_key(text, key)))

        # Seeing if we should continue
        resume = input("Would you like to decipher more with this key? "
            "(y/n) ").strip().lower()
        if (resume == "n") or (resume == "no"):
            break

    print("Decoding complete")
    return


if __name__ == '__main__':
    main()