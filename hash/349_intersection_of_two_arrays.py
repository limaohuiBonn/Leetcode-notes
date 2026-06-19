class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        hashmap = set(nums1)

        for num in set(nums2):
            if num in hashmap:
                intersection.append(num)

        return intersection