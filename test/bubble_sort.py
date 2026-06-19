def bubble_sort(ls):
    for i in range(len(ls)):
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1],ls[j]

    return ls

ls = [3, 6, 0, 13, 7, 6, 8]
print(bubble_sort(ls))
