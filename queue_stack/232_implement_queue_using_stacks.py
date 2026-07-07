class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if len(self.in_stack) == 0:
            return None
        else:
            instack = self.in_stack.copy()
            self.out_stack = self.reverse(instack)
            x = self.out_stack.pop()
            self.in_stack = self.reverse(self.out_stack.copy())
            return x

    def peek(self) -> int:
        if len(self.in_stack) > 0:
            return self.in_stack[0]
        else:
            return None

    def empty(self) -> bool:
        return True if len(self.in_stack) == 0 else False 
        
    def reverse(self, ls):
        i = 0
        j = len(ls) - 1
        while i <= j:
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1
        return ls

class MyQueue_:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack