
import tkinter as tk
from tkinter import messagebox
import random
import string
import os

# Function to generate a random password
def generate_password():
    length = int(password_length_entry.get())
    
    if length < 4:
        messagebox.showwarning("Input Error", "Password length must be at least 4 characters.")
        return

    # Character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all the character sets
    all_characters = lower_case + upper_case + digits + symbols

    # Ensure the password has a good mix by selecting at least one of each
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Add random characters to fill the rest of the password
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string
    password_str = ''.join(password)

    # Display the generated password
    password_output.config(text=password_str)

# Create the main window
root = tk.Tk()
root.title(" VISHAL Password Generator")
root.geometry("450x350")
root.configure(bg="#f0f8ff")  # Light background color

# Define a custom font for the interface
custom_font = ("Helvetica", 12, "bold")

# Heading label
heading_label = tk.Label(root, text="Random Password Generator", font=("Helvetica", 16, "bold"), fg="#333", bg="#f0f8ff")
heading_label.pack(pady=20)

# Password length label and entry
password_length_label = tk.Label(root, text="Enter Password Length:", font=custom_font, fg="#333", bg="#f0f8ff")
password_length_label.pack(pady=10)

password_length_entry = tk.Entry(root, font=custom_font, width=10, bd=2)
password_length_entry.pack(pady=5)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), fg="#3d85c6", bg="#007bff", relief="flat", command=generate_password)
generate_button.pack(pady=20)

# Label to display the generated password
password_output = tk.Label(root, text="", font=("Helvetica", 14), fg="#28a745", bg="#f0f8ff")
password_output.pack(pady=10)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_output.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 12), bg="#28a745", fg="#3d85c6", relief="flat", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Footer label
footer_label = tk.Label(root, text="Generated password contains a mix of uppercase, lowercase, digits, and symbols.", font=("Helvetica", 10), fg="#333", bg="#f0f8ff")
footer_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop() 