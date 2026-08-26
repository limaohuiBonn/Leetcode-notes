class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ']':'[', ')':'('}

        for bracket in s:
            if bracket in mapping.keys():
                if not stack or stack[-1] != mapping[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        
        return False if stack else True