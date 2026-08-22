def remove_space(s:str)->str:
    left = 0
    right = len(s) - 1

    s = list(s)

    while s[left] == ' ':
        left += 1
    
    while s[right] == ' ':
        right -= 1

    s = s[left:right+1]

    slow = fast = 0
    while fast < len(s):
        if s[fast] != ' ':
            s[slow] = s[fast]
            slow += 1
        else:
            if s[fast-1] != ' ':
                s[slow] = ' '
                slow += 1
        fast += 1
    
    return ''.join(s[0:slow])

print(remove_space(' Hello    World!'))