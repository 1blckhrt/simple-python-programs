### Password Manager ###
# A simple password manager that allows you to store, view, and remove passwords for different services.
# The program uses the Fernet symmetric encryption algorithm to encrypt and decrypt the passwords.
# The master password is used to generate a key, which is then used to encrypt and decrypt the passwords.
# The key and the encrypted master password are stored in a file called MASTER_DATA.key.
# The passwords are stored in the same file, with the service name and the encrypted password separated by a colon.
# Note: This program is for educational purposes only and should not be used for storing sensitive information.
# Note: This program requires the cryptography library to be installed. You can install it using pip: pip install cryptography.

import os
import getpass
import sys
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key_and_password(key, encrypted_password):
    with open("MASTER_DATA.key", "wb") as key_file:
        key_file.write(key + b'\n' + encrypted_password)

def load_key_and_password():
    if os.path.exists("MASTER_DATA.key"):
        with open("MASTER_DATA.key", "rb") as key_file:
            lines = key_file.read().splitlines()
            key = lines[0]
            encrypted_password = b''.join(lines[1:])
            return key, encrypted_password
    else:
        return None, None

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

def set_master():
    master_password = getpass.getpass("Please enter your master password: ")
    if not master_password:
        print("Master password cannot be empty.")
        return

    key = generate_key()
    encrypted_master_password = encrypt_data(master_password, key)
    save_key_and_password(key, encrypted_master_password)
    print("Your master password has been set. Exiting the program, please relaunch.")
    sys.exit()

def authenticate():
    while True:
        master_password = getpass.getpass("Please enter your master password: ")
        if not master_password:
            print("Master password cannot be empty.")
            continue

        key, encrypted_password = load_key_and_password()
        if not key or not encrypted_password:
            print("Master data not found. Please set a master password first.")
            return False

        decrypted_master_password = decrypt_data(encrypted_password, key)

        if master_password == decrypted_master_password:
            return True
        else:
            print("Incorrect master password. Please try again.")
            continue

def add_password():
    service = input("Enter the service name: ")
    password = getpass.getpass("Enter the password: ")
    key, _ = load_key_and_password()
    if not key:
        print("Master data not found. Please set a master password first.")
        return

    mode = "a" if os.path.exists("MASTER_DATA.key") else "w"

    with open("MASTER_DATA.key", mode) as file:
        if mode == "a":
            file.write("\n\n")
        encrypted_password = encrypt_data(password, key)
        file.write(f"{service}:{encrypted_password.decode()}\n")

    print("Password added successfully.")

def view_passwords():
    key, _ = load_key_and_password()
    if not key:
        print("Master data not found. Please set a master password first.")
        return

    with open("MASTER_DATA.key", "r") as file:
        lines = file.readlines()

    if not lines:
        print("No passwords found.")
        return

    print("\nYour Passwords:")
    for line in lines:
        if ":" not in line:
            continue

        service, encrypted_password = line.strip().split(":", 1)
        decrypted_password = decrypt_data(encrypted_password.encode(), key)
        print(f"{service}: {decrypted_password}")

def remove_password():
    key, _ = load_key_and_password()
    if not key:
        print("Master data not found. Please set a master password first.")
        return

    with open("MASTER_DATA.key", "r") as file:
        lines = file.readlines()

    if not lines:
        print("No passwords found.")
        return

    print("\nExisting Passwords:")
    service_names = []
    for line in lines:
        line = line.strip()
        if ":" not in line:
            continue

        service, _ = line.split(":", 1)
        service_names.append(service.lower())
        print(service)

    service_to_remove = input("Enter the name of the service you want to remove the password for: ").lower()

    if service_to_remove not in service_names:
        print("Service not found.")
        return

    updated_lines = [line for line in lines if not line.lower().startswith(service_to_remove + ":")]

    with open("MASTER_DATA.key", "w") as file:
        file.writelines(updated_lines)

    print("Password removed successfully.")

def change_master_password():
    while True:
        old_master_password = getpass.getpass("Enter your current master password: ")
        if not old_master_password:
            print("Master password cannot be empty.")
            continue

        key, encrypted_password = load_key_and_password()
        if not key or not encrypted_password:
            print("Master data not found. Please set a master password first.")
            return False

        decrypted_master_password = decrypt_data(encrypted_password, key)

        if old_master_password == decrypted_master_password:
            new_master_password = getpass.getpass("Set your new master password: ")
            if not new_master_password:
                print("New master password cannot be empty.")
                continue

            new_key = generate_key()
            encrypted_new_master_password = encrypt_data(new_master_password, new_key)
            save_key_and_password(new_key, encrypted_new_master_password)
            print("Your master password has been updated.")
            break
        else:
            print("Incorrect master password. Please try again.")
            continue

def main():
    print("Welcome to Password Manager!")
    if not os.path.exists("MASTER_DATA.key"):
        print("It seems like this is your first time running the program.")
        set_master()

    authenticated = False

    while True:
        if not authenticated:
            if not authenticate():
                continue
            else:
                authenticated = True

        print("\nMenu:")
        print("1. Change Master Password")
        print("2. Add Password")
        print("3: Remove Password")
        print("4. View Passwords")
        print("5. Logout and Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            change_master_password()
        elif choice == "2":
            add_password()
        elif choice == "3":
            remove_password()
        elif choice == "4":
            view_passwords()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
