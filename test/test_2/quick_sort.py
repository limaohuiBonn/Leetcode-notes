def quick_sort(nums, left, right):

    if left >= right:
        return

    mid = partition(nums, left, right)

    quick_sort(nums, left, mid - 1)
    quick_sort(nums, mid + 1, right)


def partition(nums, left, right):

    pivot = nums[right]

    fast = slow = left

    while fast < right:

        if nums[fast] < pivot:

            nums[slow], nums[fast] = nums[fast], nums[slow]

            slow += 1

        fast += 1

    nums[slow], nums[right] = nums[right], nums[slow]

    return slow
