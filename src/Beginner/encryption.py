### Encryption Program ###
# This is a simple encryption/decryption system using a Caesar cipher in Python
# In this program, the user is prompted to input a message, a key, and a mode (encrypt or decrypt)
# The program then outputs the encrypted or decrypted message, depending on the mode

def caesarCipher():
    message = input("Enter message: \n")
    key = input("Enter key (A number between 1 and 26. Positive numbers will work for both encryption and decryption.): \n")
    try:
        key = int(key)
    except:
        print("Error: please enter a key containing only numbers! No letters, special characters, or spaces are allowed! Returning to start...\n")
        return caesarCipher()
    mode = input("Enter mode (e/encrypt, d/decrypt): \n").lower()

    message = message.upper()

    if message == "" or key == "" or mode == "":
        print("Error: please enter a valid message, key, and mode! Returning to start...\n")
        return caesarCipher()

    elif message.isalpha() == False:
        print("Error: please enter a message containing only letters! No numbers, special characters, or spaces are allowed! Returning to start...\n")
        return caesarCipher()

    elif key < 1:
        print("Error: please enter a number equal to or greater than 1! Returning to start...\n")
        return caesarCipher()
    
    elif key > 26:
        print("Error: please enter a number equal to or less than 26! Returning to start...\n")
        return caesarCipher()
    
    elif mode not in ['e', 'd', 'encrypt', 'decrypt']:
        print("Error: please enter either e, encrypt or d, decrypt as the mode! Returning to start...\n")
        return caesarCipher()

    def encrypt():
        nonlocal message
        nonlocal key
        nonlocal mode
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        empty = []
        full = []

        for x in message:
            if x == ' ':
                message = message.replace(x, '')

            indexedLetter = letters.index(x)
            encryptedLetter = (indexedLetter + key) % 26
            empty.append(encryptedLetter)

            newLetter = letters[encryptedLetter]
            full.append(newLetter)

        encryptedMessage = "".join(full)

        print("\n")
        print(f"Original message: {message}")
        print(f"Encrypted message: {encryptedMessage}")

    def decrypt():
        nonlocal message
        nonlocal key
        nonlocal mode
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        empty = []
        full = []

        for x in message:
            if x == ' ':
                message = message.replace(x, '')

            indexedLetter = letters.index(x)
            encryptedLetter = (indexedLetter - key) % 26
            empty.append(encryptedLetter)

            newLetter = letters[encryptedLetter]
            full.append(newLetter)

        encryptedMessage = "".join(full)

        print("\n")
        print(f"Original message: {message}")
        print(f"Decrypted message: {encryptedMessage}")

    if mode in ['encrypt', 'e']:
        encrypt()

    elif mode in ['decrypt', 'd']:
        decrypt()

caesarCipher()