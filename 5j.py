n = int(input())
MOD = 10 ** 9 + 7
a = [0] * (n + 1)
a[0] = 1
for i in range(1, n + 1, 2):
    for j in range(i, n + 1):
        a[j] = (a[j] + a[j - i]) % MOD
print(a[n] % MOD)
