from copy import deepcopy


class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    def append(self, value):
        self.__data.append(value)
        return self.__data

    def __check_index(self, index):
        minus_bound = index < 0 and index >= -len(self.__data)
        plus_bound = 0 <= index < len(self.__data)
        is_index_valid = plus_bound or minus_bound
        if not is_index_valid:
            raise IndexError("Index is not in range.")

    def remove(self, index):
        self.__check_index(index)
        return self.__data.pop(index)

    def get(self, index):
        self.__check_index(index)
        return self.__data[index]

    def extend(self, iterable):
        self.__data.extend(iterable)
        return self.__data

    def insert(self, index, value):
        self.__check_index(index)
        self.__data.insert(index, value)
        return self.__data

    def pop(self):
        return self.__data.pop()

    def clear(self):
        self.__data.clear()

    def index(self, value):
        try:
            return self.__data.index(value)
        except ValueError:
            raise ValueError("Element is not in the list")

    def count(self, el):
        return self.__data.count(el)

    def reverse(self):
        return list(reversed(self.__data))

    def copy(self):
        return deepcopy(self.__data)

    def size(self):
        return len(self.__data)

    def add_first(self, el):
        self.__data.insert(0, el)

    def dictionize(self):
        res = {}
        for index in range(0, len(self.__data), 2):
            if len(self.__data) % 2 != 0 and index == len(self.__data) -1:
                res[self.__data[index]] = " "
            else:
                res[self.__data[index]] = self.__data[index + 1]
        return res

    def move(self, count):
        first_part = self.__data[:count]
        second_part = self.__data[count:]
        self.__data = second_part + first_part
        return self.__data

    def sum(self):
        total_sum = 0
        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                total_sum += el
            else:
                total_sum += len(el)
        return total_sum

    def overbound(self):
        max_el = float('-inf')
        searched_index = None

        for index in range(len(self.__data)):
            el = self.__data[index]
            if isinstance(el, int) or isinstance(el, float):
                if el >= max_el:
                    max_el = el
                    searched_index = index
            else:
                if len(el) >= max_el:
                    max_el = len(el)
                    searched_index = index

        return searched_index

    def underbound(self):
        min_el = float('inf')
        searched_index = None

        for index in range(len(self.__data)):
            el = self.__data[index]
            if isinstance(el, int) or isinstance(el, float):
                if el <= min_el:
                    min_el = el
                    searched_index = index
            else:
                if len(el) <= min_el:
                    min_el = len(el)
                    searched_index = index

        return searched_index
