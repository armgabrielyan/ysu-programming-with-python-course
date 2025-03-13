from collections.abc import MutableSequence

# Requires implementing __getitem__, __setitem__, __delitem__, __len__, and insert()

class CustomList(MutableSequence):
    def __init__(self, initial=None):
        self._data = list(initial) if initial else []

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def insert(self, index, value):
        self._data.insert(index, value)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"CustomList({self._data})"

cl = CustomList([1, 2, 3])
cl.append(4)   # Uses inherited append()
cl.insert(1, 99)
cl.remove(2)   # Uses inherited remove()
print(cl)

for val in cl:
    print(val)
