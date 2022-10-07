t = int(input())
for x in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    up = down = a.copy()
    down.reverse()
    b = down.copy()
    ###
    for i in range(1, n):
        tmp = up[i]
        for j in range(0, i):
            if a[j] < a[i]:
                tmp = max(tmp, up[j] + a[i])
        up[i] = tmp
    # print(*up)
    #####
    for i in range(1, n):
        tmp = down[i]
        for j in range(0, i):
            if b[j] < b[i]:
                tmp = max(tmp, down[j] + b[i])
        down[i] = tmp
    down.reverse()
    # print(*down)
    res = [up[i] + down[i] - a[i] for i in range(n)]
    print(max(res))
