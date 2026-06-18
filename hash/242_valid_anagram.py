class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic_alphabet = {}
        for i in s:
            if i not in dic_alphabet:
                dic_alphabet[i] = 1
            else:
                dic_alphabet[i] += 1

        for i in t:
            if i not in dic_alphabet:
                return False
            else:
                dic_alphabet[i] -= 1
                if dic_alphabet[i] < 0:
                    return False
            
        return True
