class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return reversed(self.iterable)


print(reversed([1, 2, 3]))

iter_a = iter([1, 2,3])
while True:
    try:
        print(next(iter_a))
    except StopIteration:
        break
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

for el in reversed([1, 2, 3]):
    print(el)

