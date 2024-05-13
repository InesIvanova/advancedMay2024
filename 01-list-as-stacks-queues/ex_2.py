expression = input()

stack = []


for index in range(0, len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        start_index = stack.pop()
        print(expression[start_index:index+1])