from pathlib import Path
from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted = Fernet(key).decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted)
    print(f"[+] Decrypted: {file_path.name}")

def decrypt_folder(folder_path):
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"❌ Error: '{folder_path}' is not a directory.")
        return

    key = load_key()
    for file_path in folder.iterdir():
        if file_path.is_file():
            decrypt_file(file_path, key)

decrypt_folder(r"C:\Users\Soham\Documents\RISE Internship Cybersecurity & Ethical Hacking Project\Ransomware_simulator\target_files")
