
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

        s = self.remove_space(s)

        # 1. 整体反转
        self.reverse(s, 0, len(s) - 1)

        # 2. 逐个单词反转
        left = 0

        for right in range(len(s)):
            if s[right] == ' ':
                self.reverse(s, left, right - 1)
                left = right + 1

        # 最后一个单词
        self.reverse(s, left, len(s) - 1)

        return ''.join(s)

    def reverse(self, s: list, left: int, right: int) -> None:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def remove_space(self, s: list) -> list:
        left = 0
        right = len(s) - 1

        while s[left] == ' ':
            left += 1

        while s[right] == ' ':
            right -= 1

        s = s[left:right + 1]

        slow = fast = 0

        while fast < len(s):
            if s[fast] != ' ':
                s[slow] = s[fast]
                slow += 1

            else:
                if s[fast - 1] != ' ':
                    s[slow] = ' '
                    slow += 1

            fast += 1

        return s[:slow]
            