## 🚀 iterator

```python
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
```

1. iterable对象只需要实现__iter__方法就可以， 它可以用python自带的iter函数来实现迭代。
2. iterator对象需要实现__iter__和__next__方法。
3. 在iterator对象中__iter__方法返回self即可，但是如果这样返回：
```python
def __iter__(self):
        # return self
        return iter(self.str)
```
就是返回python的iter方法，就没有使用MyIterator类中的__next__方法。