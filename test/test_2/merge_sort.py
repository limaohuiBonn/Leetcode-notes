def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(ls1, ls2):
    ls_new = []
    i = j = 0
    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            ls_new.append(ls1[i])
            i += 1
        else:
            ls_new.append(ls2[j])
            j += 1
        
    return ls_new
