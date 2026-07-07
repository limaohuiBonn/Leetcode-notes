class Solution_:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i in ('{','[','('):
                stack.append(i)
            elif i == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        if stack == []:
            return True
        else:
            return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'}':'{', ']':'[', ')':'('}
        for ch in s:
            if ch in pair:
                if stack and stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack