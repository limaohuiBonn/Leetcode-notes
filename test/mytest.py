class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_ls = [None]*len(nums)
        left = 0
        length = right = len(nums) - 1
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                new_ls[length] = nums[left]**2
                left += 1
            else:
                new_ls[length] = nums[right]**2
                right -= 1
            length -= 1

        return new_ls
