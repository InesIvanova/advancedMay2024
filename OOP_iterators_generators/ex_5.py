def genrange(start, end):
    while start <= end:
        yield start
        start += 1


result = genrange(1, 10)
for el in result:
    print(el)
