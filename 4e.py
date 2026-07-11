t = int(input())
for i in range(t):
    n = int(input())
    ans = set()
    s = str(n)
    s2 = s * 6
    v = 0
    z = 0
    for j in range(1, 6):
        v = int(s2[:j])
        if n == 1:
            z = 1
        else:
            if v - j >= 0:
                if (v - j) % (n - len(str(n))) == 0:
                    a = (v - j) // (n - len(str(n)))
                    b = len(str(n)) * a - j
                    if 1 <= a <= 10000 and 1 <= b <= min(10000, a * n):
                            ans.add((a, b))
    if z == 1:
        ans = set()
        for j in range(1, 10000):
            ans.add((j + 1, j))
    print(len(ans))
    for el in sorted(ans):
        print(*el)
