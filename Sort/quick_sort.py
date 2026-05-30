def quick_sort_pivot(ls, start, end):
    # serch the index of pivot
    i = start
    for j in range(start + 1, end + 1):
        if ls[j] <= ls[start]:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]

    ls[i], ls[start] = ls[start], ls[i]

    return i


def quick_sort(ls, start, end):
    if start >= end:
        return
    pivot = quick_sort_pivot(ls, start, end)
    quick_sort(ls, start, pivot - 1)
    quick_sort(ls, pivot + 1, end)
    return ls


ls = [7, 3, 2, 16, 24, 4, 11, 9]
print(quick_sort(ls, 0, len(ls) - 1))
