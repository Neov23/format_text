import os

import proper_text_formatting as ptf

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.messagebox import showinfo

# Display main window
root = tk.Tk()
root.geometry("512x384")
root.resizable(False, False)
root.title("Format Text by Dimitris Charitakis")
root.config(bg='lightgrey')
root.iconbitmap("images/ft.ico")

def select_input_file():
    """Select input file path"""
    global input_files
    global input_directory

    # Get filepath and store value in input-entry StringVar
    input_files = []
    file_path = askopenfilename()
    input_path.set(file_path)

    # From file-path get filename
    filename = os.path.basename(file_path)

    # Store file name as element in a list
    input_files.append(filename)

    # Get directory path of file
    input_directory = os.path.dirname(file_path)
    print(input_directory)

def select_input_directory():
    """Select input directory path"""
    global input_files
    global input_directory

    # Get directory path and store value in input-entry StringVar
    input_files = []
    input_directory = askdirectory()
    input_path.set(input_directory)

    # Store each file name as element in a list
    for file in os.listdir(input_directory):
        if file.endswith(".txt"):
            input_files.append(file)

def select_output_directory():
    """Select output directory path"""
    output_directory = askdirectory()
    output_path.set(output_directory)

def convert_clicked():
    """Callback when the convertion button is clicked"""
    # Call format_text from ptf module
    ptf.format_text(input_directory, output_path.get(), input_files)

    # Showinfo
    msg = f'Path to output directory: {output_path.get()}'
    showinfo(
        title="Info",
        message=msg
    )

def main_info():
    """Describe the program"""
    msg = ("You should select a local text file from your PC, then select a "
            "directory and filename for the file that will be created.\n\n"
            "This program reads your selected text file, and formats it in a "
            "way, that every text-line has maximum 80 characters.\n\n")
    showinfo(
        title="Info",
        message=msg
    )

# Create input label
input_label = tk.Label(root, text="Load File or Folder:",
                        font=("Arial", 16))
input_label.config(bg='lightgrey')
input_label.place(relx=0.5, rely=0.08, anchor="n")

# Create input file-path button
btn_input_file = ttk.Button(root, text="Choose File...", width=17,
                            command=select_input_file)
btn_input_file.place(relx=0.38, rely=0.24, anchor='n')

# Create input directory-path button
btn_input_directory = ttk.Button(root, text="Choose Folder...", width=17,
                            command=select_input_directory)
btn_input_directory.place(relx=0.62, rely=0.24, anchor='n')

# Create readonly entry and display StringVar connected to input buttons
input_path = tk.StringVar()
input_path_entry = tk.Entry(root, textvariable=input_path,
                        font=("Arial", 11), bd=0, state="readonly", width=40)
input_path_entry.place(relx=0.5, rely=0.16, anchor='n')

# Create output label
output_label = tk.Label(root, text="Save output at Folder:",
                        font=("Arial", 16))
output_label.config(bg='lightgrey')
output_label.place(relx=0.5, rely=0.4, anchor='n')

# Create output directory-path button
btn_output_directory = ttk.Button(root, text="Choose Folder...", width=17,
                            command=select_output_directory)
btn_output_directory.place(relx=0.5, rely=0.56, anchor='n')

# Create readonly entry and display StringVar connected to output button
output_path = tk.StringVar()
output_path_entry = tk.Entry(root, textvariable=output_path,
                        font=("Arial", 11), bd=0, state="readonly", width=40)
output_path_entry.place(relx=0.5, rely=0.48, anchor='n')

# Create convert button (sends above data to ptf.format_text and displays info)
btn_convert = tk.Button(root, text="Convert", command=convert_clicked)
btn_convert.config(width=20, bg='green', font=("Arial", 14, "bold"))
btn_convert.place(relx=0.5, rely=0.78, anchor='n')

# Create an info button to describe the program to user
btn_info = tk.Button(root, text="Info", width=5, command=main_info)
btn_info.place(relx=0.95, rely=0.95, anchor='se')

# Run main program
root.mainloop()