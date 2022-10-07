x = [0 for _ in range(105)]
dp = [x.copy() for _ in range(105)]
dp[0][0] = dp[1][0] = dp[0][1] = dp[1][1] = 1


# for i in range(5):
#     for j in range(5):
#         print(dp[i][j], end=' ')
#     print()


def cal(a, i):
    res = 0
    for j in range(0, i):
        res += a[j][i - j - 1]
    if i % 2 == 1 and i >= 5:
        res -= a[int(i / 2)][int(i / 2)]
        res += a[int(i / 2)][int(i / 2)] ** 2
    return res


for i in range(2, 105):
    dp[i][i] = cal(dp, i)
    for j in range(0, i + 1):
        if j != i - j:
            dp[j][i - j] = dp[j][j] * dp[i - j][i - j]

t = int(input())
for x in range(t):
    n = int(input())
    print(dp[n][n])
