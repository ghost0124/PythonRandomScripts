def consecutive_zeros(s):
    b = 0
    c = 0
    i = 0

    for i in range(len(s)):
        if int(s[i]) == 0:
            b += 1
        else:
            if b >= c:
                c = b
            b = 0

    if c < b :
        return b
    else:
        return c

print(consecutive_zeros("101"))
print('\n')
print(consecutive_zeros("0"))
print('\n')
print(consecutive_zeros("1001101000110"))