
# * build a new string

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         ls = s.split()
#         new_s = ''
#         for idx in range(len(ls)-1,-1,-1):
#             new_s += ls[idx]
#             if idx != 0:
#                 new_s += ' '
#         return new_s

# * update in place

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        while s[left] == ' ':
                left += 1
        while s[right] == ' ':
                right -= 1

        s = s[left:right+1]
        self.reverse(s)
        
        i = 0
        j = 0


        for j in range(len(s)):
            if s[j] != '':
                  j += 1
            self.reverse(s[i:j])
            i = j + 1
        return ''.join(s)

    def reverse(self, s: list) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
