tc = int(input())
for t in range(tc):
    n, m = [int(x) for x in input().split()]
    a = []
    dp = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
        dp.append([0 for _ in range(m)])
    dp[0][0] = a[0][0]
    for i in range(n):
        for j in range(m):
            if i == 0 and j != 0:
                dp[i][j] = a[i][j] + dp[i][j - 1]
            elif j == 0 and i != 0:
                dp[i][j] = a[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = a[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    print(dp[n - 1][m - 1])
