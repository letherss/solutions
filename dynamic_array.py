class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 4
        self._array = [None] * self._capacity

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._size

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, item):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._array[self._size] = item
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty dynamic array")
        self._size -= 1
        item = self._array[self._size]
        self._array[self._size] = None
        return item

    def __getitem__(self, index):
        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise IndexError("DynamicArray index out of range")
        return self._array[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise IndexError("DynamicArray assignment index out of range")
        self._array[index] = value

if __name__ == "__main__":
    a = DynamicArray()
    a.capacity
    for x in range(5):
        a.append(x * 10)
    len(a)
    a.capacity
    a[4]
    a[1] = 99
    a.pop()
    len(a)
    a.capacity
    a[4]
