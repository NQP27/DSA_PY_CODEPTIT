tc = int(input())
for t in range(tc):
    n = int(input())
    x, y, z = [int(c) for c in input().split()]
    dp = [0 for _ in range(n + 1)]
    """x: insert     y: delete      z: copy   """
    dp[1] = x
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + x, dp[int(i / 2)] + z)
        else:
            dp[i] = min(dp[i - 1] + x, dp[int((i + 1) / 2)] + y + z)
    print(dp[n])
