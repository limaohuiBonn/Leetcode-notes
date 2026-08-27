## 🚀 decorator

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end -start
        print(f'the processing time is {elapsed}')
        return result
    return wrapper

@timer
def add(a,b):
    return a + b

print(add(3,4))
```

1. decorator就是在函数中定义函数，主函数的输入是方法指针，返回值是内部定义函数（wrapper）的入口地址。
2. 内部定义函数的输入就是被修饰的方法的参数，然后加上魔法糖（例子中就是统计函数运行时间）。