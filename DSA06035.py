
# t = int(iF.readline())
t = int(input())
for x in range(0, t):
    # n = int(iF.readline())
    n=int(input())
    a = [int(i) for i in input().split()]
    # a = [int(i) for i in iF.readline().split()]
    # print(*a)
    # print('')
    min_pos = []
    p = []
    if a[0] < a[1]:
        min_pos.append(0)
    else:
        p.append(1)
    for i in range(1, n - 1):
        if a[i] < a[i + 1] and a[i] < a[i - 1]:
            min_pos.append(i)
            p.append(0)
        else:
            if a[i] > a[i - 1] and a[i] > a[i + 1]:
                p.append(1)
            else:
                p.append(0)
    if a[n - 2] > a[n - 1]:
        min_pos.append(n - 1)
        p.append(0)
    else:
        p.append(1)
    print(*p)
    print(*min_pos)
    res = 0
    for i in range(0, len(min_pos) - 1):
        b = p[min_pos[i]:min_pos[i + 1]:1]
        print(*b)
        if any(b):
            res = max(res, min_pos[i + 1] - min_pos[i] + 1)
    if len(min_pos) == 0:
        res = n
    if len(min_pos) == 1:
        res = n - min_pos[0]
    print(res)
