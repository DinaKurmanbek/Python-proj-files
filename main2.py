
# from cryptography.fernet import Fernet
# secret_key = b'pSDPS_QlljeNhB3yCUNQqt4UamhurVByqcF7w4Zcj9o='
#
# f = Fernet(secret_key)
# encrypted = b'gAAAAABlag7qLdgxrGgNXeylOfCqXq40Wz8eDrUpt_WXXJ-mwcARkvzKJY9k3gwOD6IW1G-v0z3sLipR5BBGdu6fSFq3Gosk0Q=='
#
# decrypted = f.decrypt(encrypted)
# print(decrypted)

# with open("spy.key", "rb") as f:
#     d = f.read()
#
# print(d)
#
# with open("spy_reports", "b") as f:
#     d = f.read()
#
# print(d)

for day in range(1, 32):
    print(f"{day:02d}_10_2023_")