class MyIterator:
    def __init__(self, _string):
        self._str = _string
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self._str):
            char = self._str[self.idx]
            self.idx += 1
            return char
        else:
            raise StopIteration

def mygenerator(_string):
    for char in _string:
        yield char


