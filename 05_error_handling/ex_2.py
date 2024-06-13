word = input()

try:
    n = int(input())
except ValueError as ex:
    print("Variable times must be an integer")
else:
    print(word * n)




