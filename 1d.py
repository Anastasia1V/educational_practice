t = int(input())
for i in range(t):
    n = int(input())
    x = 2
    v = 3
    if n > 0:
        print(1, end=' ')
        n -= 1
    for i in range(n):
        print(x * v, end=' ')
        x = v
        v += 1
        z = 0
        while z == 0:
            z = 1
            go = 2
            while go * go <= v:
                if v % go == 0:
                    z = 0
                    break
                go += 1
            if z == 0:
                v += 1
    print()
