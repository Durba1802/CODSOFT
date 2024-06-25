
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string


def generate_password(): # Function to generate password
    try:
        length = int(length_entry.get())  # Get password length from entry field
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        return
    
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return
    
    complexity = complexity_combobox.current()  # Get complexity selection index
    
    if complexity == 0:
        
        characters = string.ascii_letters   # Letters only
    elif complexity == 1:
       
        characters = string.ascii_letters + string.digits  # Letters + Digits
    elif complexity == 2:
     
        characters = string.ascii_letters + string.digits + string.punctuation    # Letters + Digits + Symbols
    
   
    password = ''.join(random.choice(characters) for _ in range(length)) # Generate password
    
   
    password_var.set(password)   # Display generated password


window = tk.Tk()
window.title("Password Generator App")  # Create main tkinter window

# Frame for password length
length_frame = ttk.Frame(window, padding="10") 
length_frame.grid(row=0, column=0, sticky="w")

length_label = ttk.Label(length_frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")

length_entry = ttk.Entry(length_frame, width=10)
length_entry.grid(row=0, column=1, padx=5)

# Frame for password complexity
complexity_frame = ttk.Frame(window, padding="10")
complexity_frame.grid(row=1, column=0, sticky="w")

complexity_label = ttk.Label(complexity_frame, text="Complexity:")
complexity_label.grid(row=0, column=0, sticky="w")

# Combobox for complexity options
complexity_options = ["Letters Only", "Letters + Digits", "Letters + Digits + Symbols"]
complexity_combobox = ttk.Combobox(complexity_frame, values=complexity_options, width=20, state="readonly")
complexity_combobox.current(0)  # Set default selection
complexity_combobox.grid(row=0, column=1, padx=5)

# Button to generate password
generate_button = ttk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, pady=10)

# Frame to display generated password
password_frame = ttk.Frame(window, padding="10")
password_frame.grid(row=3, column=0, sticky="w")

password_label = ttk.Label(password_frame, text="Generated Password:")
password_label.grid(row=0, column=0, sticky="w")

password_var = tk.StringVar()
password_entry = ttk.Entry(password_frame, textvariable=password_var, width=30, state="readonly")
password_entry.grid(row=0, column=1, padx=5)

# Start the tkinter main loop
window.mainloop()  
  

