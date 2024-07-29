from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        result = function()
        return [el for el in result if el in 'aeouiy']
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]





print(get_letters())

print(get_letters)

print(get_letters)

