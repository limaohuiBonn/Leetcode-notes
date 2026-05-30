class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap_s = self.composeHashmap(s)
        for val in t:
            if val in hashmap_s.keys():
                hashmap_s[val] -= 1
            else:
                hashmap_s[val] = -1

        for s in hashmap_s.items():
            if s[1] == -1:
                return s[0]

    def composeHashmap(self, string_: str) -> dict:
        hashmap = {}
        for val in string_:
            if val in hashmap.keys():
                hashmap[val] += 1
            else:
                hashmap[val] = 1
        return hashmap
