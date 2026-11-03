class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        if len(self.item) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if self.is_empty == 0:
            raise IndexError("Стек пуст")
        return self.item.pop()

    def peek(self):
        if self.peek == 0:
            raise IndexError("Стек пуст")
        return self.item[-1]

    def size(self):
        return len(self.item)

if __name__ == "__main__":
    s = Stack()
    s.is_empty()  # True
    s.push(1)
    s.push(2)
    s.push(3)
    s.size()  # 3
    s.peek()  # 3
    s.pop()  # 3
    s.pop()  # 2
    s.is_empty()  # False
