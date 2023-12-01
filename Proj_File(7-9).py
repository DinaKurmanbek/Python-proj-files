

from cryptography.fernet import Fernet
import os

path = "C:/Users/777/PycharmProjects/pythonProject5/decrypted_reports"
output_path = "C:/Users/777/PycharmProjects/pythonProject5/encrypted_reports"
key = Fernet.generate_key()
print(key)

def encrypt(content, key):
    f = Fernet(key)
    encrypted_content = f.encrypt(content.encode())
    return encrypted_content

def select_files(path, key):
    for file_name in os.listdir(path):
        if "c" not in file_name.lower():
            file_path = os.path.join(path, file_name)

            with open(file_path, "rb") as file:
                content = file.read().decode("utf-8")

            encrypted = encrypt(content, key)

            original_file_name, _ = os.path.splitext(file_name)
            output_file_path = os.path.join(output_path, f"{original_file_name}_encrypted.txt")

            with open(output_file_path, "wb") as f:
                f.write(encrypted)

select_files(path, key)