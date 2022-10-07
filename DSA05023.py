tc = int(input())
for t in range(tc):
    s = input()
    n = len(s)
    dp = [0 for _ in range(n)]
    dp[0] = int(s[0])
    for i in range(1, n):
        dp[i] = dp[i - 1]
        tmp = int(s[i])
        sum = 0
        sum += tmp
        for j in range(i - 1, -1, -1):
            tmp = int(s[j]) * (10 ** (i - j)) + tmp
            sum += tmp
        dp[i] += sum
    print(dp[n - 1])
