class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_len = float('-inf')
        i = 0
        str_ls = []
        for j in range(len(s)):
            while s[j] in str_ls:
                str_ls.pop(0)
                i += 1

            str_ls.append(s[j])
            sub_len = max(sub_len, j-i+1)

        return sub_len if sub_len != float('-inf') else 0    