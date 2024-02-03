import os
import getpass
import ast
import sys
from simplecrypt import encrypt, decrypt
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt

master_password_set = False  # Flag to track whether the master password has been set

def generate_key(master_password):
    salt = get_random_bytes(16)
    return scrypt(master_password, salt, 32, N=2**14, r=8, p=1)

def save_key(key):
    try:
        with open("MASTER_KEY.key", "wb") as key_file:
            key_file.write(key)
    except Exception as e:
        print("Error occurred while saving the key:", e)
        sys.exit()

def load_key():
    try:
        if os.path.exists("MASTER_KEY.key"):
            with open("MASTER_KEY.key", "rb") as key_file:
                return key_file.read()
        else:
            return None  # Return None if the key file is not found
    except Exception as e:
        print("Error occurred while loading the key:", e)
        sys.exit()

def encrypt_data(data, key):
    return encrypt(key, data)

def decrypt_data(encrypted_data, key):
    return decrypt(key, encrypted_data)

def set_master():
    global master_password_set

    if load_key():
        print("You already have a master password, if you want to change it please login and change it!")
        sys.exit()
    else:
        master_password_input = getpass.getpass("Please enter your master password:")

        if not master_password_input:
            print("Master password cannot be empty. Operation canceled.")
            sys.exit()

        key = generate_key(master_password_input)
        if key:
            save_key(key)
            print("Your master password has been set. Exiting the program, please relaunch.")
            sys.exit()
        else:
            print("Error generating the key.")
            sys.exit()

def load_decrypted():
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "rb") as file:
            return file.read()
    else:
        return b""

def change_master_password():
    global master_password_set

    master_password_input = getpass.getpass("Enter your current master password: ")

    key = load_key()

    if key is None:
        print("No master key found. Please create a new one.")
        return

    if master_password_input == decrypt_data(load_decrypted(), key):
        new_master_password = getpass.getpass("Set your new master password: ")

        new_key = generate_key(new_master_password)

        if new_key:
            try:
                # Delete the old key
                os.remove("MASTER_KEY.key")
                
                # Save the new key
                save_key(new_key)
                
                print("Your master password has been updated.")
                
                # Update the global master_password_set flag
                master_password_set = True  
            except Exception as e:
                print("Error occurred while updating the key:", e)
                sys.exit()
        else:
            print("Error generating the key.")
            sys.exit()
    else: 
        print("Incorrect password!")
        return

def save_encrypted(data):
    with open("passwords.txt", "wb") as file:
        file.write(data)

def add_password(passwords, service, password):
    passwords[service] = password

def main():
    global master_password_set

    passwords = {}
    key = load_key()

    if key is None:
        set_master()

    elif not master_password_set:
        has_password = input("Do you have a master password? (yes/y, no/n)").lower()

        if has_password == "yes" or has_password == "y":
            master_password = getpass.getpass("Enter your master password: ")

            # Verify if the entered master password is correct
            decrypted_password = decrypt_data(load_decrypted(), key)
            print("Decrypted password:", decrypted_password)
            print("Entered master password:", master_password)
            if master_password != decrypted_password:
                raise ValueError("Incorrect master password!")


        elif has_password == "no" or has_password == "n":
            set_master()

        else: 
            print("Not a valid input!")
            sys.exit()
        master_password_set = True

    while True:

        print("\nPassword Manager Actions:")
        print("1. Add password")
        print("2. View passwords")
        print("3. Change master password")
        print("4. Exit")

        choice = input("What would you like to do? ")

        if choice == "1":
            service = input("Enter the service name: ")
            password = getpass.getpass("Enter the password: ")
            add_password(passwords, service, password)
            encrypted_passwords = encrypt_data(str(passwords), key)
            save_encrypted(encrypted_passwords)
            print("\nPassword added successfully.")

        elif choice == "2":
            decrypted_data = decrypt_data(load_decrypted(), key)
            if decrypted_data:
                stored_passwords = ast.literal_eval(decrypted_data)
                if len(stored_passwords) == 1 and "master_password" in stored_passwords:
                    print("\nNo passwords stored yet other than the master password.")
                else:
                    print("Stored Passwords:")
                    for service, password in stored_passwords.items():
                        print(f"\nService: {service}, Password: {password}")
            else:
                print("\nNo passwords stored yet.")

        elif choice == "3":
            change_master_password()

        elif choice == "4":
            print("Exiting...")


if __name__ == "__main__":
    main()
