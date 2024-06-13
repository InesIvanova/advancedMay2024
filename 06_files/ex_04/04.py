import os

path = os.path.join("..", "ex_03", "my_first_file.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File does not exist")