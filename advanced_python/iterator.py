from collections.abc import Iterable, Iterator

class MyIterator:
    def __init__(self, num):
        self.num = num
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.num:
            number = self.cur
            self.cur += 1
            return number
        else:
            raise StopIteration

for i in MyIterator(5):
    print(i)