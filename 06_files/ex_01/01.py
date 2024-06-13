import os
from constants import ABSOLUTE_PROJECT_PATH

try:
    path = os.path.join("text.txt")
    file = open(path)
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")


file_path = os.path.join(ABSOLUTE_PROJECT_PATH, "05_error_handling", "example_file.txt")
print(file_path)
# With absolute path
# import os
# from constants import ABSOLUTE_PROJECT_PATH
# path = os.path.join(ABSOLUTE_PROJECT_PATH, "06_files", "ex_01", "text.txt")
# try:
#     open(path)
#     print("File found")
# except FileNotFoundError:
#     print("File not found")
