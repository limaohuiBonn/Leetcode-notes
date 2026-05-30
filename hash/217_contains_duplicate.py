class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap.keys():
                return True
            hashmap[num] = i
        else:
            return False
