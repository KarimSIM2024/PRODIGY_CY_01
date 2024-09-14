import tkinter as tk
from tkinter import messagebox

# Function to encrypt the text
def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Function to decrypt the text
def decrypt(text, shift):
    return encrypt(text, -shift)

# Function to handle the encryption button click
def handle_encrypt():
    text = entry_message.get()
    shift = int(entry_shift.get())
    encrypted_message = encrypt(text, shift)
    label_result.config(text=f"Encrypted: {encrypted_message}")

# Function to handle the decryption button click
def handle_decrypt():
    text = entry_message.get()
    shift = int(entry_shift.get())
    decrypted_message = decrypt(text, shift)
    label_result.config(text=f"Decrypted: {decrypted_message}")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher GUI")

# Create and place the message label and entry field
label_message = tk.Label(root, text="Enter your message:")
label_message.pack()

entry_message = tk.Entry(root, width=50)
entry_message.pack()

# Create and place the shift value label and entry field
label_shift = tk.Label(root, text="Enter the shift value:")
label_shift.pack()

entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

# Create and place the Encrypt button
button_encrypt = tk.Button(root, text="Encrypt", command=handle_encrypt)
button_encrypt.pack()

# Create and place the Decrypt button
button_decrypt = tk.Button(root, text="Decrypt", command=handle_decrypt)
button_decrypt.pack()

# Label to display the result
label_result = tk.Label(root, text="")
label_result.pack()

# Run the application
root.mainloop()
