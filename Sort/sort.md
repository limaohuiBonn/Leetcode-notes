## 🚀 merge sort

```python
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
```

1. 首先要实现一个函数可以合并两个有序数组，可以利用双指针分别指向两个数组。
2. 主函数是一个递归，不断将数据拆分成两个，直到只有一个元素。然后对只有一个元素的数组进行合并。

## 🚀 quick sort
```python
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
```

1. 首先实现一个函数，如何进行快速排序。首先将数组的最后一位定义为pivot,作为参考点。定义两个指针slow,fast，fast指针遇到比pivot大的数，pivot就指向下一个。如果fast指向了一个比pivot小的数，那么slow和fast指针指向的对象进行交换。slow和fast指针都指向下一个。最后将pivot值和slow指针指向的元素进行交换，返回slow的位置。
2. 主函数进行递归，如果left大于right就返回。调用快速排序函数，得到mid,然后分别递归左右两个部分。