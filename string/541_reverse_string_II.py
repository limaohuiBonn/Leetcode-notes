class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        new_s = ''
        for idx,i in enumerate(range(0, len(s), k)):
            if idx % 2 == 0:
                new_s += ''.join(self.reverse(s[i:i+k]))
            else:
                new_s += ''.join(s[i:i+k])
        
        return new_s

    def reverse(self, s:str)->list:
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s