def bubble_sort_v1(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
        print(ls)
    return ls


def bubble_sort_v2(ls):
    for i in range(len(ls) - 1, -1, -1):
        for j in range(0, i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
        print(ls)
    return ls


ls = [3, 6, 0, 13, 7, 6, 8]
print(bubble_sort_v2(ls))
