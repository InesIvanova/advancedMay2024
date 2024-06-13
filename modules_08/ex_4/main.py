from modules_08.ex_4.core import mapper, truncate_decimal_part_till_digit

expression = input()

num_as_string, sign, num_2_as_string = expression.split()
num1 = float(num_as_string)
num2 = int(num_2_as_string)


result = mapper[sign](num1, num2)


if isinstance(result, str):
    print(result)
else:
    result = truncate_decimal_part_till_digit(result, 2)
    print(f"{result:.2f}")
