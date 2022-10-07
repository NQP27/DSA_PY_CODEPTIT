t = int(input())
for x in range(0, t):
    n = int(input())
    a = [int(i) for i in input().split()]
    dp = a.copy()
    res = a[0]
    for i in range(1, n):
        tmp = dp[i]
        for j in range(0, i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], tmp + dp[j])
        res = max(res, dp[i])
    print(res)