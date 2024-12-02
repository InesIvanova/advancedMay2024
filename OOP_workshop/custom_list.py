from copy import deepcopy

from OOP_workshop.custom_exceptions import IndexOutOfRange, ElementNotPresented, EmptyList


class CustomList:
    def __init__(self, *args):
        self.__value = list(args)

    def append(self, value):
        self.__value.append(value)
        return self.__value


    def remove(self, index):
        if not (0 <= index < len(self.__value)):
            raise IndexOutOfRange("Invalid index")
        return self.__value.pop(index)

    def get(self, index):
        if not (0 <= index < len(self.__value)):
            raise IndexOutOfRange("Invalid index")
        return self.__value[index]

    def index(self, element):
        try:
            return self.__value.index(element)
        except ValueError:
            raise ElementNotPresented("Element not presented")

    def final_index(self, element):
        for index in range(len(self.__value) -1, -1, -1):
            if self.__value[index] == element:
                return index
        raise ElementNotPresented("Element not presented")

    def extend(self, iterable):
        self.__value.extend(iterable)
        return self.__value

    def insert(self, index, value):
        if not (0 <= index < len(self.__value)):
            raise IndexOutOfRange("Invalid index")
        self.__value.insert(index, value)
        return self.__value

    def pop(self):
        if not self.__value:
            raise EmptyList("No elements in the list")
        return self.__value.pop()

    def clear(self):
        self.__value.clear()

    def count(self, element):
        return self.__value.count(element)

    def reverse(self):
        return list(reversed(self.__value))

    def copy(self):
        return deepcopy(self.__value)

    def size(self):
        return len(self.__value)

    def add_first(self, value):
        self.__value.insert(0, value)

    def dictionize(self):
        data = {}

        for index in range(0, len(self.__value), 2):
            key = self.__value[index]
            try:
                value = self.__value[index+1]
            except IndexError:
                value = " "
            data[key] = value
        return data

    def move(self, amount):
        result = self.__value[amount:] + self.__value[:amount]
        return result

    def sum(self):
        total_sum = 0
        for el in self.__value:
            if isinstance(el, int) or isinstance(el, float):
                total_sum += el
            else:
                total_sum += len(el)

        return  total_sum

    def overbound(self):
        max_num = float("-inf")
        biggest_index = None

        for index in range(len(self.__value)):
            if isinstance(self.__value[index], int) or isinstance(self.__value[index], float):
                to_compare = self.__value[index]
            else:
                to_compare = len(self.__value[index])

            if to_compare >= max_num:
                max_num = to_compare
                biggest_index =  index

        return biggest_index

    def underbound(self):
        min_num = float("inf")
        smallest_index = None

        for index in range(len(self.__value)):
            if isinstance(self.__value[index], int) or isinstance(self.__value[index], float):
                to_compare = self.__value[index]
            else:
                to_compare = len(self.__value[index])

            if to_compare <= min_num:
                min_num = to_compare
                smallest_index =  index

        return smallest_index
