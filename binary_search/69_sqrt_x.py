class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0
        while left <= right:
            middle = (left + right) // 2
            square = middle * middle
            if square > x:
                right = middle - 1
            elif square <= x:
                left = middle + 1
                ans = middle
        return ans
