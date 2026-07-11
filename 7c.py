t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    if sum(a) <= k:
        ans = n
    else:
        go1 = 0
        go2 = n - 1
        v1 = a[go1]
        v2 = a[go2]
        while True:
            if k < 1 or go1 > go2:
                break
            if go1 == go2:
                if k >= v1:
                    ans += 1
                break
            m = min(v1, v2)
            if k >= 2 * m:
                k -= 2 * m
                v1 -= m
                v2 -= m
                if v1 == 0:
                    go1 += 1
                    ans += 1
                    if go1 <= go2:
                        v1 = a[go1]
                if v2 == 0:
                    go2 -= 1
                    ans += 1
                    if go1 <= go2:
                        v2 = a[go2]
            else:
                v1 -= (k + 1) // 2
                v2 -= k // 2
                if v1 < 1:
                    go1 += 1
                    ans += 1
                if v2 < 1:
                    go2 -= 1
                    ans += 1
                k = 0
    print(ans)
