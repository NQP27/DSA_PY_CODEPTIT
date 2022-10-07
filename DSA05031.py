import math

dp = [i for i in range(0, 10000 + 1)]
for i in range(1, 10000 + 1):
    if int(math.sqrt(dp[i])) ** 2 == dp[i]:
        dp[i] = 1
    else:
        for j in range(1, i):
            dp[i] = min(dp[i], dp[j] + dp[i - j])
tc = int(input())
for t in range(tc):
    n = int(input())
    print(dp[n])
