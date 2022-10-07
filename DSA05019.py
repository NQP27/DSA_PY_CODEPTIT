t = int(input())
for x in range(t):
    n, m = [int(x) for x in input().split()]
    a = []
    dp = []
    res = 0
    for i in range(n):
        a.append([int(x) for x in input().split()])
        dp.append(a[i].copy())
    for i in range(1, n):
        for j in range(1, m):
            if a[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                res = max(res, dp[i][j])
    print(res)

    # print(*a)
