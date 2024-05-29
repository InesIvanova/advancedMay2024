from functools import reduce


def sum_nums(a, b):
    return a + b

lambda a,b: a + b



def multiply(*args):
    # [int(el) for el in ['1', '2']]
    # list(map(int, ['1', '2']))
    # return reduce(lambda x, y: x * y, args)

    total = 1
    for num in args:
        total *= num
    return total


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
