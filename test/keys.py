class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = index = len(nums) - 1
        sorted_ls = [0] * len(nums)
        while i <= j:
            square_i = nums[i] * nums[i]
            square_j = nums[j] * nums[j]
            if square_i < square_j:
                sorted_ls[index] = square_j
                j -= 1
            else:
                sorted_ls[index] = square_i
                i += 1
            index -= 1
        return sorted_ls

                

