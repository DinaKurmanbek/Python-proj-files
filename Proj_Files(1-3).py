from cryptography.fernet import Fernet
import os

with open("spy.key", "rb") as f:
    key = f.read()
fernet = Fernet(key)

import os

folder_path = "C:/Users/777/PycharmProjects/pythonProject5/spy_reports"
output_folder = "C:/Users/777/PycharmProjects/pythonProject5/decrypted_reports"
all_files = os.listdir(folder_path)


def check_files(folder_path, output_folder):
    for day in range(1, 32):  # Assuming days in October range from 1 to 31
        prefix = f"{day:02d}_10_2023_"
        # Filter files that start with the specified prefix
        matching_files = [file for file in all_files if file.startswith(prefix) and file.endswith(".txt")]

        if matching_files:
            #print(f"Files exist for October {day}")
            for file_name in matching_files:
                input_file_path = os.path.join(folder_path, file_name)
                with open(input_file_path, "rb") as file:
                    report = file.read()
                decrypted = fernet.decrypt(report)
                #print(decrypted)

                original_file_name, _ = os.path.splitext(file_name)
                output_file_path = os.path.join(output_folder, f"{original_file_name}.txt")

                with open(output_file_path, "wb") as f:
                    f.write(decrypted)
        else:
            print(f"No files found for October {day}")



check_files(folder_path, output_folder)

