t = int(input())
for x in range(t):
    s = input()
    n = len(s)
    s = 'x' + s
    a = [0 for _ in range(n + 2)]
    dp = [a.copy() for _ in range(n + 2)]
    res = 1
    for i in range(1, n + 1):
        dp[i][i] = 1

    for l in range(2, n + 1):
        for i in range(n - l + 2):
            j = i + l - 1
            if l == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            if dp[i][j] == 1:
                res = max(res, l)
    print(res)
