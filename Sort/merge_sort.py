def merge(ls1, ls2):
    ls = []
    i = 0
    j = 0
    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            ls.append(ls1[i])
            i += 1
        else:
            ls.append(ls2[j])
            j += 1

    ls.extend(ls1[i:])
    ls.extend(ls2[j:])
    return ls


def merge_sort(ls):
    if len(ls) == 1:
        return ls
    mid = len(ls) // 2
    left = merge_sort(ls[:mid])
    right = merge_sort(ls[mid:])
    return merge(left, right)


ls = [7, 3, 2, 16, 24, 4, 11, 9]
print(merge_sort(ls))
