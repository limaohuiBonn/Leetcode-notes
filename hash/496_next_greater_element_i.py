class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack[-1]] = num
                stack.pop()
            else:
                stack.append(num)

        while stack:
            hashmap[stack[-1]] = -1
            stack.pop()

        return [hashmap[val] for val in nums1]
