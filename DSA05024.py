mod = int(1e9 + 7)
tc = int(input())
for t in range(tc):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    dp = [0 for _ in range(m + 1)]
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(0, n):
            if i >= a[j]:
                dp[i] = (dp[i] % mod + dp[i - a[j]] % mod) % mod
            dp[i] %= mod
    print(int(dp[m]))
