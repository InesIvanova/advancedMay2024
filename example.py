def calculator(operator):
    def addition(a, b):
        return a + b
    def subtraction(a, b):
        return a - b


    if operator == "+":
        return addition
    elif operator == "-":
        return subtraction



result = calculator("+")
print(result(4, 5))