class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx,num in enumerate(nums):
            expect = target - num
            if expect in hashmap:
                return [hashmap[expect], idx]
            else:
                hashmap.update({num:idx})
            