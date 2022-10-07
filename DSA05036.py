tc = int(input())
for t in range(tc):
    n = int(input())
    a = [0]
    b = [0]
    for i in range(n):
        x, y = [float(j) for j in input().split()]
        a.append(x)
        b.append(y)
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    res = 1
    for i in range(2, n + 1):
        tmp = 1
        for j in range(1, i):
            if a[i] > a[j] and b[i] < b[j]:
                tmp = max(tmp, dp[j] + 1)
        dp[i] = tmp
        res = max(res, dp[i])
    print(res)
