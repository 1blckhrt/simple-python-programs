### Encryption Program ###
# This is a simple encryption/decryption system using a Caesar cipher in Python
# In this program, the user is prompted to input a message, a key, and a mode (encrypt or decrypt)
# The program then outputs the encrypted or decrypted message, depending on the mode

def caesarCipher():
    message = input("Enter message: \n")
    key = input("Enter key (A number between 1 and 26. Negative signs (-) are not necessary.): \n")
    try:
        key = int(key)
    except:
        raise ValueError("Please enter a valid number between 1 and 26! Returning to start...")
    mode = input("Enter mode (e/encrypt, d/decrypt): \n").lower()

    message = message.upper()
    message = message.replace(" ", "")

    if not message or not key or not mode:
        print("Error: please enter a valid message, key, and mode! Returning to start...\n")
        return caesarCipher()
    
    elif not message.isalpha():
        print("Error: please enter a message with only letters! Returning to start...\n")
        return caesarCipher()

    elif key < 1 or key > 26:
        print("Error: please enter a number between 1 and 26! Returning to start...\n")
        return caesarCipher()
    
    elif mode not in ['e', 'd', 'encrypt', 'decrypt']:
        print("Error: please enter either e, encrypt or d, decrypt as the mode! Returning to start...\n")
        return caesarCipher()

    def cipher():
        nonlocal message
        nonlocal key
        nonlocal mode
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        empty = []
        full = []

        for x in message:
            indexedLetter = letters.index(x)

            if mode in ['encrypt', 'e']:
                messageLetter = (indexedLetter + key) % 26

            else:
                messageLetter = (indexedLetter - key) % 26
                
            empty.append(messageLetter)

            newLetter = letters[messageLetter]
            full.append(newLetter)

        finalMessage = "".join(full)

        print(f"\nOriginal Message: {message}")

        if mode in ['encrypt', 'e']:
            print(f"Encrypted Message: {finalMessage}")

        else:
            print(f"Decrypted Message: {finalMessage}")
        
    cipher()
caesarCipher()