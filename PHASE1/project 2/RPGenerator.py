import tkinter as tk
import random
import string

def generate_random_password():
    length = int(length_entry.get())
    uppercase = uppercase_var.get()
    lowercase = lowercase_var.get()
    digits = digits_var.get()
    special_chars = special_chars_var.get()

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        result_label.config(text="Select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_result_var.set(password)

root = tk.Tk()
root.title(" Password Generator")
root.geometry("700x370")  # Adjusted the height
root.config(bg="green")
# Labels
length_label = tk.Label(root, text="Password Length:", font=("Times New Roman", 20, "bold"),bg="grey")
length_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Times New Roman", 20, "bold"),bg="green")
result_label.pack(pady=5)

# Entry
length_entry = tk.Entry(root, font=("Times New Roman", 20, "bold"),bg="orange")
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # Default length

# Checkboxes (Single Line)
checkbox_frame = tk.Frame(root)
checkbox_frame.pack()

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(checkbox_frame, text="Uppercase", variable=uppercase_var, font=("Lucidia", 20, "bold"),bg="green")
lowercase_check = tk.Checkbutton(checkbox_frame, text="Lowercase", variable=lowercase_var, font=("Lucidia", 20, "bold"),bg="green")
digits_check = tk.Checkbutton(checkbox_frame, text="Digits", variable=digits_var, font=("Lucidia", 20, "bold"),bg="green")
special_chars_check = tk.Checkbutton(checkbox_frame, text="Special Characters", variable=special_chars_var, font=("Lucidia", 20, "bold"),bg="green")

uppercase_check.pack(side=tk.LEFT)
lowercase_check.pack(side=tk.LEFT)
digits_check.pack(side=tk.LEFT)
special_chars_check.pack(side=tk.LEFT)

# Button
generate_button = tk.Button(root, text="Generate Password", height=2, width=20, font=("Times New Roman", 20, "bold"),bg="chocolate4" ,command=generate_random_password)
generate_button.pack(pady=10)

# Password Result
password_result_var = tk.StringVar()
password_result = tk.Entry(root,bg="chocolate4", textvariable=password_result_var, state="readonly", font=("Times New Roman", 20, "bold"))
password_result.pack(pady=5)

root.mainloop()
