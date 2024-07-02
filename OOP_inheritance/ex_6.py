from typing import List


class Stack:
    def __init__(self) -> None:
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return True if not self.data else False

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"


s = Stack()
print(s.is_empty())
print(s.data)
s.push("a")
s.push("b")
s.push("c")
print(s.is_empty())
print(s.data)
print(s)
s.pop()
print(s)
print(s.top())
print(s)