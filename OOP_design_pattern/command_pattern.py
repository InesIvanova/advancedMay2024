from abc import ABC, abstractmethod


class AbstractRule(ABC):
    @abstractmethod
    def check(self, file):
        pass


class HeaderRule(AbstractRule):
    def check(self, file):
        columns = file.columns()
        return columns == ['name', 'age', 'location']


class DataTypeRule(AbstractRule):
    def check(self, file):
        mapper = {'name': str, 'age': int, 'location': str}

        all_names = file['name']
        are_names_valid = all([isinstance(name, str) for name in all_names])

        return are_names_valid


class DataValidityRule(AbstractRule):
    def check(self, file):
        all_names = file['name']
        valid_names = [name for name in all_names if 2<= len(name) <=50]
        return len(all_names) == len(valid_names)




rules = (HeaderRule(), DataTypeRule(), DataValidityRule())


class RuleExecutor:
    def __init__(self, file):
        self.file = file

    def execute(self):
        for rule in rules:
            rule.check(self.file)