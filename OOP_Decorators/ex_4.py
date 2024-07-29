def multiply(number):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * number
        return wrapper
    return decorator

@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
