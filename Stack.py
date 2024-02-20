import pytest


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty == False:
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def test_1():
    s = Stack()
    s.push(3)
    result = s.peek()
    assert result == 3
    assert s.pop() == 3


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.stack)
    s.pop()
    print(s.stack)
    print(s.size())
    print(s.peek())
    test_1()

