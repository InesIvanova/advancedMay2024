class vowels:
    def __init__(self, string):
        self.string = string
        self.all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        # self.vowels_from_string = [el for el in self.string if el.lower() in self.all_vowels]
        self.current_index = -1
    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index == len(self.string):
            raise StopIteration
        if self.string[self.current_index].lower() in self.all_vowels:
            return self.string[self.current_index]
        else:
            return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
