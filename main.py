
from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()
print(f"key: {secret_key}")

fernet_key = Fernet(secret_key)
print(f"fernet_key : {fernet_key}")

data = b"Hello World"
encrypted_data = fernet_key.encrypt(data)
print(encrypted_data)

decrypted_data = fernet_key.decrypt(encrypted_data)
print(decrypted_data)