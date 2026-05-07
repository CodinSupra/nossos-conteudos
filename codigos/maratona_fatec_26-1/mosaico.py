def mosaico():
    p = int(input())
    b = 0
    m = 1
    if p in range(1, 1001):
        if p < 8:
            return 0
        while True:
            p_n = 4 * m + 4
            if p >= p_n:
                b += m * m
                p -= p_n
                m += 1
            else:
                break
    return b

print(mosaico())