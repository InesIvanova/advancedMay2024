def create_sequence(n):
    fibb = [0, 1]

    for _ in range(n-2):
        current_num = fibb[-1] + fibb[-2]
        fibb.append(current_num)
    return fibb


def locate_number(seq, number):
    try:
        return seq.index(number)
    except ValueError:
        return f"The number {number} is not in the sequence"