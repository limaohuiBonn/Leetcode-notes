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