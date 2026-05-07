def estimativa():
    us = int(input())
    media = int(input())
    est = str(input()).split()
    custo = 0
    for i in range(us):
        custo += int(est[i])
        if custo > media:
            custo -= int(est[i])
            break
        if custo < media:
            custo += int(est[i + 1])
            if custo > media:
                custo -= int(est[i])
                break
            us += 1
    return f'{us}\n{custo}'

print(estimativa())