class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap_AB = {}
        hashmap_CD = {}
        count = 0

        for i in nums1:
            for j in nums2:
                sum_2 = i + j
                if sum_2 not in hashmap_AB:
                    hashmap_AB[sum_2] = 1
                else:
                    hashmap_AB[sum_2] += 1

        for i in nums3:
            for j in nums4:
                sum_2 = i + j
                if sum_2 not in hashmap_CD:
                    hashmap_CD[sum_2] = 1
                else:
                    hashmap_CD[sum_2] += 1

        for i in hashmap_AB:
            if -i in hashmap_CD:
                count += hashmap_AB[i] * hashmap_CD[-i]
        
        return count

