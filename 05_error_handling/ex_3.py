class ValueCannotBeNegative(Exception):
    """Use for numbers below 0"""
    pass


def int(arg):
    # cast the arg
    raise ValueError()

int("asd")

for _ in range(5):
    n = int(input())

    if n < 0:
        raise ValueCannotBeNegative