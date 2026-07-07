def remove_space(s):
    i = j = 0
    s = list(s)
    for i in range(len(s)):
        if i != ' ':
            j = i
        