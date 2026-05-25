class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in hashtable:
                return [hashtable[need], i]
            else:
                hashtable[num] = i
