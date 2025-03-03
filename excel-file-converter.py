### Excel File Converter ###
# This program converts .xls files to .xlsx files
# The user is prompted to select a file through File Explorer, the program then converts it to an .xlsx file

import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def rename_file():
    file_path = filedialog.askopenfilename()

    if not file_path:
        print("You didn't select a file.")
        return

    if not file_path.lower().endswith(".xls"):
        print("Please select a valid .xls file!")
        return rename_file()

    file_name, file_extension = os.path.splitext(file_path)
    new_file = file_name + ".xlsx"

    try:
        os.rename(file_path, new_file)
        print(f"File renamed successfully as {new_file}\n")
        print(f"The file can be found at {os.getcwd()}. Opening the folder the file is in now...")
        new_file_path = os.path.abspath(new_file)
        subprocess.Popen(['explorer', '/select,"{}"'.format(new_file_path)])

    except FileNotFoundError:
        print(f'File {file_path} not found! Please try again.')

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    rename_file()
