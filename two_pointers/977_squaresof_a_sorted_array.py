class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        index = j = len(nums) - 1
        new_ls = [0] * len(nums)
        while i <= j:
            square_i = nums[i] * nums[i]
            square_j = nums[j] * nums[j]
            if square_j > square_i:
                new_ls[index] = square_j
                j -= 1
            elif square_j <= square_i:
                new_ls[index] = square_i
                i += 1
            index -= 1
        return new_ls
