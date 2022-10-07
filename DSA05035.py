dp = []
tmp = [0, 10]
res = [0, 10]
for i in range(2):
    dp.append([1 for _ in range(10)])
for i in range(2, 101):
    dp.append([0 for _ in range(10)])
for i in range(2, 101):
    tm = 0
    for j in range(1, 10):
        if j == 1 and i == 2:
            dp[i][j] = 9
        elif j == 1:
            dp[i][j] = tmp[i - 1]
        else:
            dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]
        tm += dp[i][j]
    tmp.append(tm)
    res.append(tm + res[i - 1])

tc = int(input())
for t in range(tc):
    n = int(input())
    print(int(res[n] % (1e9 + 7)))
