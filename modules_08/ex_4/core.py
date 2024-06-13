def truncate_decimal_part_till_digit(number, n):
    result = str(number).split(".")
    first_part, decimal_point = result
    decimal_point = decimal_point[:n]
    result = float(f'{first_part}.{decimal_point}')
    return result


def sum_nums(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Can not divide by 0"


def multiply_nums(a, b):
    return a * b


def power(a, b):
    return a ** b


mapper = {
    "+": sum_nums,
    "-": subtract,
    "*": multiply_nums,
    "/": divide,
    "^": power
}