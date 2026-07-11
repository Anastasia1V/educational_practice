s = input()
s2 = s[::-1]
b = 31
mod = 10 ** 8 + 7
n = len(s)
pow_b = [1] * (n + 1)
for i in range(1, n + 1):
    pow_b[i] = pow_b[i - 1] * b % mod
pat_hash = [0] * (n + 1)
for i in range(n):
    pat_hash[i + 1] = (pat_hash[i] * b + ord(s[i]) - ord('a') + 1) % mod
cur_hash = [0] * (n + 1)
for i in range(n):
    cur_hash[i + 1] = (cur_hash[i] * b + ord(s2[i]) - ord('a') + 1) % mod
for i in range(n, 0, -1):
    a = pat_hash[i]
    a2 = (cur_hash[n] - cur_hash[n - i] * pow_b[i]) % mod
    if a == a2:
        print(i)
        break
