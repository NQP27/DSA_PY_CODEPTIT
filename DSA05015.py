import math


def modInverse(b, x):
    g = math.gcd(b, x)
    if g != 1:
        return -1
    else:
        return pow(b, x - 2, x)


def modDivide(a, b, x):
    a = a % x
    inv = modInverse(b, x)
    if inv != -1:
        print((inv * a) % x)


t = int(input())
dp = [0, 1]
m = 10 ** 9 + 7
for i in range(2, 1001):
    dp.append(dp[i - 1] * i)
for x in range(t):
    n, k = (int(x) for x in input().split())
    if n < k:
        print(0)
    elif n > k:
        modDivide(dp[n], dp[n - k], m)
