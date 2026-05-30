def select_sort(ls):
    for i in range(len(ls) - 1):
        index = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[index]:
                index = j
        ls[i], ls[index] = ls[index], ls[i]

    return ls


ls = [3, 6, 0, 13, 7, 6, 8]
print(select_sort(ls))
