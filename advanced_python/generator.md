## 🚀 generator
```python
def mygenerator(num):
    for i in range(num):
        yield (i**2)
```

1. 本质就是return和yield的区别。return直接返回所有返回值，而yield则是在next方法的调用下一个一个生成。