import os
from constants import ABSOLUTE_PROJECT_PATH


path_to_file = os.path.join(ABSOLUTE_PROJECT_PATH, "06_files", "text.txt")

file = open(path_to_file)
file.write("\nfrom with statement")
with open(path_to_file, "a") as file:
    file.write("\nfrom with statement")
print(file.closed)

