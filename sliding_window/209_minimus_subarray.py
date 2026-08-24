
# ? two for loops
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sub = float('inf')
        for i in range(len(nums)):
            total = 0
            for j in range(i,len(nums)):
                total += nums[j]
                if total  >= target:
                    sub = min(sub,j-i+1)
                    break
        if sub == float('inf'):
            sub = 0
        return sub



class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sub_len = float('inf')
        total = 0
        i = 0
        for j in range(len(nums)):
            total += nums[j]
            while total >= target:
                sub_len = min(sub_len, j-i+1)
                total -= nums[i]
                i += 1
        return sub_len if sub_len != float('inf') else 0

