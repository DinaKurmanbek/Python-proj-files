
from cryptography.fernet import Fernet
import os

path = "C:/Users/777/PycharmProjects/pythonProject5/decrypted_reports"


def replace_prefix(word, prefix, replacement):
    if word.startswith(prefix):
        return replacement + word[len(prefix):]
    return word

def modify_and_save(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)  #  To consoleeeee
        words = content.split()
        modified_words = [replace_prefix(word, "вра", "дру") for word in words]
        modified_words = [replace_prefix(word, "Вра", "Дру") for word in modified_words]
        modified_content = ' '.join(modified_words)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)

    # Add a new line indicating whether modifications were made
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("\nПроверено!")
        # if modified_content != content:
        #     file.write("\nПроверено! Есть изм")
        # else:
        #     file.write("\nПроверено! Без изм")

def change(path):
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        modify_and_save(file_path)
    print(f"\n Modifications saved to files from {path}")

# Call the function with your folder path
change(path)


