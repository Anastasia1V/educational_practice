n, m, k = map(int, input().split())
a = list()
for i in range(n + 1):
    a.append(set())
for i in range(k):
    x, y = map(int, input().split())
    a[x].add(y)
MOD = 10**9 + 7
dp = [0] * (m + 1)
dp[0] = 1
for i in range(n + 1):
    for j in range(m + 1):
        if i != 0 or j != 0:
            if j in a[i]:
                dp[j] = 0
            else:
                ans = dp[j]
                if j > 0:
                    ans += dp[j - 1]
                dp[j] = ans % MOD
print(dp[m])
