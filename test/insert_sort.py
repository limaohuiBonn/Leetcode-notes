def insert_sort(ls):
    for i in range(1, len(ls)):
        cur = ls[i]
        j = i - 1
        while j >=0 and ls[j] > cur:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = cur
    return ls

ls = [3, 6, 0, 13, 7, 6, 8]
print(insert_sort(ls))
