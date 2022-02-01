import proper_text_formatting as ptf

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

# Display main window
root = tk.Tk()
root.geometry("512x384")
root.resizable(False, False)
root.title("Format Text by Dimitris Charitakis")
root.config(bg='lightgrey')

def select_input_file():
    """Select input file path"""
    file_selected = askopenfilename()
    input_filename.set(file_selected)

def select_output_file():
    """Select output directory path"""
    directory_selected = asksaveasfilename()
    output_directory.set(f"{directory_selected}.txt")

def convert_clicked():
    """Callback when the convertion button is clicked"""
    msg = f'Path to new file: {output_directory.get()}'
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
input_label = tk.Label(root, text="File Path:", font=("Arial", 16))
input_label.config(bg='lightgrey')
input_label.place(relx=0.5, rely=0.08, anchor="n")

# Create input browsing button
input_browser = ttk.Button(root, text="Browse", command=select_input_file)
input_browser.place(relx=0.5, rely=0.24, anchor='n')

# Display input path (create StringVar connected to it's label & browse button)
input_filename = tk.StringVar(input_browser)
input_path_label = tk.Entry(root, textvariable=input_filename,
                        font=("Arial", 11), bd=0, state="readonly", width=40)
input_path_label.config(bg='lightgrey')
input_path_label.place(relx=0.5, rely=0.16, anchor='n')

# Create output label
output_label = tk.Label(root, text="File Destination (without extension):",
                        font=("Arial", 16))
output_label.config(bg='lightgrey')
output_label.place(relx=0.5, rely=0.4, anchor='n')

# Create output browsing button
output_browser = ttk.Button(root, text="Browse", command=select_output_file)
output_browser.place(relx=0.5, rely=0.56, anchor='n')

# Display output path (create StringVar connected to it's label & browse button)
output_directory = tk.StringVar(output_browser)
output_path_label = tk.Entry(root, textvariable=output_directory,
                        font=("Arial", 11), bd=0, state="readonly", width=40)
output_path_label.place(relx=0.5, rely=0.48, anchor='n')

# Create convert button (sends above data to ptf.format_text and displays info)
convert_button = tk.Button(root, text="Convert",
                command=lambda:[ptf.format_text(input_filename.get(),
                            f"{output_directory.get()}"), convert_clicked()])
convert_button.config(width=20, bg='green', font=("Arial", 14, "bold"))
convert_button.place(relx=0.5, rely=0.78, anchor='n')

# Create an info button to describe the program to user
info_button = tk.Button(root, text="Info", width=5, command=main_info)
info_button.place(relx=0.95, rely=0.95, anchor='se')

# Run main program
root.mainloop()